from turtle import distance
import torch
import torch.nn as nn
import transformers.models.bart.modeling_bart as bart

from machine_learning.service_scrap.transformer.GBST_Extended import GBST_Extended
from machine_learning.service_scrap.transformer.compressive_transformer_pytorch import CompressiveTransformer
# from machine_learning.exter_dataset.uitls.fuzzy_logic import fuzzy_NOT


class Pooler(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.dense = nn.Linear(hidden_size, hidden_size)
        self.activation = nn.Tanh()

    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        # We "pool" the model by simply taking the hidden state corresponding
        # to the first token.
        first_token_tensor = hidden_states[:, 0]
        pooled_output = self.dense(first_token_tensor)
        pooled_output = self.activation(pooled_output)
        return pooled_output


class NN_Video(nn.Module):
    def __init__(self):
        pass


class NN_Audio(nn.Module):
    def __init__(self):
        pass


class NN_Image(nn.Module):
    def __init__(self):
        pass


class NN_PlainTextConfig(nn.Module):
    def __init__(self, num_tokens=257, num_lang=64, num_type=10, downsample_factor=4, score_consensus_attn=True, max_block_size=4, dim=512, seq_len=1024, depth=12, emb_dim=None, memory_layers=None, enhanced_recurrence=True, mem_len=1024, cmem_len=1024 // 4, cmem_ratio=4, heads=8, gru_gated_residual=True, mogrify_gru=False, attn_dropout=0., ff_glu=False, ff_dropout=0., attn_layer_dropout=0., reconstruction_attn_dropout=0., reconstruction_loss_weight=1, blocks=None):
        self.num_tokens = num_tokens
        self.num_lang = num_lang
        self.num_type = num_type
        self.downsample_factor = downsample_factor
        self.score_consensus_attn = score_consensus_attn
        self.max_block_size = max_block_size
        self.dim = dim
        self.seq_len = seq_len
        self.depth = depth
        self.emb_dim = emb_dim
        self.memory_layers = memory_layers
        self.enhanced_recurrence = enhanced_recurrence
        self.mem_len = mem_len
        self.cmem_len = cmem_len
        self.cmem_ratio = cmem_ratio
        self.heads = heads
        self.gru_gated_residual = gru_gated_residual
        self.mogrify_gru = mogrify_gru
        self.attn_dropout = attn_dropout
        self.ff_glu = ff_glu
        self.ff_dropout = ff_dropout
        self.attn_layer_dropout = attn_layer_dropout
        self.reconstruction_attn_dropout = reconstruction_attn_dropout
        self.reconstruction_loss_weight = reconstruction_loss_weight
        self.max_block_size = max_block_size
        self.downsample_factor = downsample_factor
        self.score_consensus_attn = score_consensus_attn
        self.blocks = blocks


class Pooler(nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.dense = nn.Linear(hidden_size, hidden_size)
        self.activation = nn.Tanh()

    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        # We "pool" the model by simply taking the hidden state corresponding
        # to the first token.
        first_token_tensor = hidden_states[:, 0]
        pooled_output = self.dense(first_token_tensor)
        pooled_output = self.activation(pooled_output)
        return pooled_output


class NN_Plain_Text(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.tokenizer = GBST_Extended(num_tokens=257, num_type=257, num_lang=257,
                                       dim=512, max_block_size=4, downsample_factor=4, score_consensus_attn=True)
        self.transformer = CompressiveTransformer(emb_dim=128, dim=512,    depth=12,    seq_len=1024,    mem_len=1024, cmem_len=1024 // 4, cmem_ratio=4, reconstruction_loss_weight=1,
                                                  attn_dropout=0.1, ff_dropout=0.1, attn_layer_dropout=0.1, gru_gated_residual=True, mogrify_gru=False, memory_layers=range(6, 13), ff_glu=True)
        self.types = {"Text": 0, "Html": 1, "Xhtml": 2, "Discord": 3, "Twitter": 4, "Facebook": 5, "Gab": 6, "Tumblr": 7, "Truth": 8, "Snapchat": 9, "Pinterest": 10, "Parler": 11, "Myspace": 12, "Micro.blog": 13,
                      "MeWe": 14, "LiveJournal": 15, "Instagram": 16, "GNU social": 17, "Gettr": 18, "Gab": 19, "Friendica": 20, "23snaps": 21, "Diaspora": 22, "TSV": 23, "CSV": 24, "XML": 25, "JSON": 26, "YAML": 27, "wikitext": 28}
        self.langs = {"en":0}

    def forward(self, tensor_text, tensor_types, lang, mask=None):
        chars = []
        types = []
        langs = []
        for i in bytes(tensor_text, 'utf-8'):
            chars.append(i)
            types.append(self.types[tensor_types])
            langs.append(self.langs[lang])
        tensor_text = torch.tensor([chars])
        tensor_types = torch.tensor([types])
        tensor_langs = torch.tensor([langs])
        x, mask = self.tokenizer(tensor_text, tensor_types, tensor_langs, mask=mask)
        out, mem, aux_loss = self.transformer(x, mask=mask)
        return out, mem, aux_loss


class NN_EvidenceCheck(nn.Module):
    def __init__(self):
        self.text = NN_Plain_Text()
        self.transformer = CompressiveTransformer(emb_dim=128, dim=512,    depth=12,    seq_len=1024,    mem_len=1024, cmem_len=1024 // 4, cmem_ratio=4, reconstruction_loss_weight=1,
                                                  attn_dropout=0.1, ff_dropout=0.1, attn_layer_dropout=0.1, gru_gated_residual=True, mogrify_gru=False, memory_layers=range(6, 13), ff_glu=True)

        self.transformer_qerry = CompressiveTransformer(emb_dim=128, dim=512,    depth=12,    seq_len=1024,    mem_len=1024, cmem_len=1024 // 4, cmem_ratio=4, reconstruction_loss_weight=1,
                                                        attn_dropout=0.1, ff_dropout=0.1, attn_layer_dropout=0.1, gru_gated_residual=True, mogrify_gru=False, memory_layers=range(6, 13), ff_glu=True)
        self.pooler = Pooler(512)
        self.cos = nn.CosineSimilarity(dim=512, eps=1e-6)

    def forward(self, x, memories=None, mask=None, evidences=None, train=False):

        out_qerry, mem, aux_loss = self.transformer_qerry(
            x, memories=memories, mask=mask)
        if train:
            relevance_best_distance = 1
            not_relevance_best_distance = 0
            for evidence in evidences:
                out, memories, aux_loss = self.text(
                    *evidence["args"], **evidence["keywords"])
                out, mem, aux_loss = self.transformer(out, memories=memories)
                distance = self.cos(self.pooler(out_qerry), self.pooler(out))
                if bool(evidence["relevance"]):
                    if distance < relevance_best_distance:
                        relevance_best_distance = distance
                else:
                    if distance > not_relevance_best_distance:
                        not_relevance_best_distance = fuzzy_NOT(distance)
            return out_qerry, mem, aux_loss, (relevance_best_distance, not_relevance_best_distance)
        else:
            # DB LOOKUP
            return out_qerry, mem, aux_loss, None


class NN_Translator(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self):
        pass


class NN_FactCheck(nn.Module):
    def __init__(self):
        self.text = NN_Plain_Text()
        self.transformer = CompressiveTransformer(emb_dim=128, dim=512,    depth=12,    seq_len=1024,    mem_len=1024, cmem_len=1024 // 4, cmem_ratio=4, reconstruction_loss_weight=1,
                                                  attn_dropout=0.1, ff_dropout=0.1, attn_layer_dropout=0.1, gru_gated_residual=True, mogrify_gru=False, memory_layers=range(6, 13), ff_glu=True)
        self.transformer_query = CompressiveTransformer(emb_dim=128, dim=512,    depth=12,    seq_len=1024,    mem_len=1024, cmem_len=1024 // 4, cmem_ratio=4, reconstruction_loss_weight=1,
                                                        attn_dropout=0.1, ff_dropout=0.1, attn_layer_dropout=0.1, gru_gated_residual=True, mogrify_gru=False, memory_layers=range(6, 13), ff_glu=True)
        self.cos = nn.CosineSimilarity(dim=1, eps=1e-6)
        self.pool_answer = Pooler(512)
        self.pool_query = Pooler(512)

    def forward(self, x, memories=None, mask=None, evidences=None):
        L = []
        for evidence in evidences:
            out_query, mem, aux_loss = self.transformer_query()
            out_query = self.pool_query(out_query)
            distance_best = 1
            B = []
            for evidence in evidences:
                if evidence["type"] == "text":
                    out_answer, mem, aux_loss = self.text(
                        *evidence["arg"], **evidence["keywords"])
                    out_answer = self.pool_answer(out_answer)
                    distance = self.cos(out_query, out_answer)
                    B.append({
                        "distance": distance,
                        "evidence type": distance,
                    })
                if distance < distance_best:
                    best_answer = out_answer
                    best_mem = mem
                    best_aux_loss = aux_loss
            B.append(L)
        for evidence in evidences:
            evidence["distance"]
            # NOT
            fuzzy_NOT(evidence["distance"])
