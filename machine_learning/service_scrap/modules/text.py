import torch
import torch.nn as nn
from machine_learning.service_scrap.modules.GBST_Extended import GBST_Extended
from machine_learning.service_scrap.modules.UpperTokenizer import UpperTokenizer
from machine_learning.service_scrap.modules.compressive_transformer_pytorch import CompressiveTransformer
import machine_learning.service_scrap.modules.variables as variables

class TextEncoder(nn.Module):
    def __init__(self,num_tokens,num_type,num_lang,dim,max_block_size, downsample_factor,score_consensus_attn,emb_dim,depth,seq_len,mem_len,cmem_len,reconstruction_loss_weight,attn_dropout,ff_dropout,attn_layer_dropout,gru_gated_residual,mogrify_gru,memory_layers,one_head_kv,ff_glu):
        super().__init__()
        self.text_tokenizer = GBST_Extended(num_tokens = num_tokens,num_type=num_type,num_lang=num_lang,dim = dim,max_block_size = max_block_size, downsample_factor = downsample_factor,score_consensus_attn = score_consensus_attn)    
        self.text_encoder = CompressiveTransformer(
            emb_dim = emb_dim,
            dim = dim,
            depth = depth,
            seq_len = seq_len,
            mem_len = mem_len,
            cmem_len = cmem_len,
            reconstruction_loss_weight = reconstruction_loss_weight,
            attn_dropout = attn_dropout,
            ff_dropout = ff_dropout,
            attn_layer_dropout = attn_layer_dropout,
            gru_gated_residual = gru_gated_residual,
            mogrify_gru = mogrify_gru,
            memory_layers = memory_layers ,
            ff_glu = ff_glu
        )
        self._tokenizer = UpperTokenizer()
    def forward(self,text,lang= None,type_= None):
        # x = self._tokenizer(text,lang,type_)
        # need to add lang and type
        byte_text = list(bytes(text, 'UTF-8'))
        types = []
        langs = []
        for i in byte_text:
            types.append(variables.type_dict[type_])
            langs.append(variables.lang_dict[lang])
        mask   = torch.ones(1, len(byte_text)).bool()
        types = torch.tensor([types])
        langs = torch.tensor([langs])
        x = torch.tensor([byte_text])
        tokens, mask = self.text_tokenizer(x,x_type=types,x_lang=langs,mask=mask)
        return self.text_encoder(tokens,mask=mask)

text_encoder = TextEncoder(variables.num_tokens,variables.num_type,variables.num_lang,variables.dim,variables.max_block_size, variables.downsample_factor,variables.score_consensus_attn,variables.emb_dim,variables.depth,variables.seq_len,variables.mem_len,variables.cmem_len,variables.reconstruction_loss_weight,variables.attn_dropout,variables.ff_dropout,variables.attn_layer_dropout,variables.gru_gated_residual,variables.mogrify_gru,variables.memory_layers,variables.one_head_kv,variables.ff_glu)
