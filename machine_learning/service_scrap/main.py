import torch
import torch.nn as nn
from transformer.ExpireSpan.ExpireSpan import ExpireSpan
from transformer.charformer_encoder.GBST import GBST, exists
from transformer.charformer_encoder.GBST_Extended import GBST_Extended
from transformer.compressive_transformers.compressive_transformer_pytorch import FeedForward, GRUGating, PreNorm, SelfAttention, default, iterate_tensor, to


class text_encoder_layer(torch.nn.Module):
    def __init__(self,dim,seq_len, mem_len, cmem_len, cmem_ratio, heads, ff_dropout, ff_glu,  attn_layer_dropout,  attn_dropout,  reconstruction_attn_dropout, mogrify=False,ramp_length = 128):
        super().__init__()
        self.expire_span = ExpireSpan(dim,mem_len, ramp_length)
        self.attn_layers = PreNorm(dim,GRUGating(dim, SelfAttention(dim, seq_len, mem_len, cmem_len, cmem_ratio, heads, dropout = attn_layer_dropout, attn_dropout = attn_dropout, reconstruction_attn_dropout = reconstruction_attn_dropout)))
        self.ff_layers = PreNorm(dim, GRUGating(dim,FeedForward(dim, dropout = ff_dropout, glu = ff_glu)))
    def forward(self, x, memories_rnn = None, pos_emb = None, input_mask = None, calc_memory_rrn = True,mem_expand=None, time=None,n=None):
        if x is None:
            n = x.shape
        if exists(mem_expand):
            exps, expire_mask = self.expire_span(mem_expand, time, seq_len = n) 
        else:
            exps, expire_mask = (None, input_mask)
        mask =  input_mask.logical_and(expire_mask)
        x, mem, aux_loss = self.attn_layers(x, memories = memories_rnn, pos_emb = pos_emb, input_mask = mask, calc_memory = calc_memory_rrn)
        x,  =  self.ff_layers(x)
        
        if exists(exps):
            expiring_exps_mask = (expire_mask > 0) & (expire_mask < 1.)
            expiring_exps = exps.masked_select(expiring_exps_mask[..., :-n])
            aux_loss = aux_loss + (expiring_exps / self.seq_len).sum() * self.expire_loss_coef
        return x, mem, aux_loss,exps

 
class text_encoder(torch.nn.Module):
    def __init__(self,num_tokens,num_tokens_lang,num_tokens_type,dim,seq_len,depth,emb_dim = None,memory_layers = None,enhanced_recurrence = True,mem_len = None,cmem_len = None,cmem_ratio = 4,heads = 8,gru_gated_residual = True,mogrify_gru = False,attn_dropout = 0.,ff_glu = False,ff_dropout = 0.,attn_layer_dropout = 0.,reconstruction_attn_dropout = 0.,reconstruction_loss_weight = 1.,max_block_size = 4,downsample_factor = 4,score_consensus_attn = True) -> None:
        super().__init__()
        emb_dim = default(emb_dim, dim)
        mem_len = default(mem_len, seq_len)
        cmem_len = default(cmem_len, mem_len // cmem_ratio)
        memory_layers = default(memory_layers, list(range(1, depth + 1)))        
        assert mem_len >= seq_len, 'length of memory should be at least the sequence length'
        assert cmem_len >= (mem_len // cmem_ratio), f'length of compressed memory should be at least the memory length divided by the compression ratio {int(mem_len // cmem_ratio)}'
        assert all([layer > 0 and layer <= depth for layer in memory_layers]), 'one of the indicated memory layers is invalid'
        self.seq_len = seq_len
        self.depth = depth
        self.memory_layers = list(memory_layers)
        self.enhanced_recurrence = enhanced_recurrence
        if emb_dim == dim:
            self.to_model_dim = nn.Identity() 
        else:
            self.to_model_dim = nn.Linear(emb_dim, dim)
        seq_and_mem_len = seq_len + mem_len + cmem_len
        self.pos_emb = nn.Parameter(torch.zeros(heads, seq_and_mem_len, dim // heads))
        layers = []
        self.emb = GBST_Extended(num_tokens,num_tokens_lang,num_tokens_type,dim,downsample_factor = downsample_factor,score_consensus_attn = score_consensus_attn,max_block_size=max_block_size)
        for i in range(depth):
            layers.append(text_encoder_layer(dim,seq_len, mem_len, cmem_len, cmem_ratio, heads, ff_dropout, ff_glu,  attn_layer_dropout,  attn_dropout,  reconstruction_attn_dropout))
        self.layers = nn.ModuleList(layers)
        self.dim = dim
    
    def forward(self, x_tex,x_type,x_lang, memories_rnn = None,memory_span=None, mask = None):
        b, n, d, device = *x_tex.shape, self.dim, x_tex.device
        print(x_type)
        x_tex , mask = self.emb(x_tex,x_type,x_lang,mask)
        memories_rnn = default(memories_rnn, (None, None))
        mems_layers = memory_span.mems if exists(memory_span) else ((None,) * self.depth)
        times_layers = memory_span.elapsed_times if exists(memory_span) else ((None,) * self.depth)
        mem_rrn, cmem_rnn = memories_rnn
        # x = self.to_model_dim(x)

        next_mem = []
        next_cmem = []
        aux_loss = torch.tensor(0., requires_grad = True, **to(x_tex))

        # if self.enhanced_recurrence:
        #     mem = torch.roll(mem, -1, 0)
        #     cmem = torch.roll(cmem, -1, 0)
        
        b, t, d = x_tex.shape
        num_memory_layers = len(self.memory_layers)
        init_empty_mem = lambda: torch.empty(num_memory_layers, b, 0, d, **to(x_tex))
        mem_rrn = default(mem_rrn, init_empty_mem)
        cmem_rnn = default(cmem_rnn, init_empty_mem)
        total_len = mem_rrn.shape[2] + cmem_rnn.shape[2] + self.seq_len
        pos_emb = self.pos_emb[:, (self.seq_len - t):total_len]
        mem_iter, cmem_iter = map(iterate_tensor, (mem_rrn, cmem_rnn))
        for ind, (mem_expand, time, layer) in enumerate(zip(mems_layers, times_layers,self.layers)):
            layer_num = ind + 1
            use_memory = layer_num in self.memory_layers
            memories_rnn = (next(mem_iter), next(cmem_iter)) if use_memory else None
            x_tex, (mem_out, cmem_out), layer_aux_loss, exps = layer(x_tex, memories_rnn = memories_rnn, calc_memory_rrn = use_memory, input_mask = mask, pos_emb = pos_emb,mem_expand=mem_expand)
            aux_loss = aux_loss + layer_aux_loss
            if not use_memory:
                continue
            next_mem.append(mem_out)
            next_cmem.append(cmem_out)
        next_mem, next_cmem = map(torch.stack, (next_mem, next_cmem))
        next_mem, next_cmem = map(torch.detach, (next_mem, next_cmem))
        return x_tex, (mem_out, cmem_out), layer_aux_loss

model = text_encoder(num_tokens = 1024,num_tokens_lang = 1024,num_tokens_type = 1024,emb_dim = 256,dim = 512,depth = 12,seq_len = 1024,mem_len = 1024,cmem_len = 1024 // 4,cmem_ratio = 4,reconstruction_loss_weight = 1,attn_dropout = 0.1,ff_dropout = 0.1,attn_layer_dropout = 0.1,gru_gated_residual = True,mogrify_gru = False,     memory_layers = range(6, 13),ff_glu = True)
# inputs = torch.randint(0, 256, (1, 2048))
# print(inputs)
# masks = torch.ones_like(inputs).bool()
# x_lang = inputs.reshape(1, -1, 1024).transpose(0, 1)
# x_type = inputs.reshape(1, -1, 1024).transpose(0, 1)
# x_text = inputs.reshape(1, -1, 1024).transpose(0, 1)
# masks = masks.reshape(1, -1, 1024).transpose(0, 1)
# logits, memories, aux_loss = model(x_text[0],x_type[0],x_lang[0], mask = masks[0])

import torch.optim as optim
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)