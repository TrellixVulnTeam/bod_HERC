import torch
import torch.nn as nn
from machine_learning.service_scrap.modules.compressive_transformer_pytorch import CompressiveTransformer
from machine_learning.service_scrap.modules.text import text_encoder
from machine_learning.service_scrap.modules.middle_layer import middleLayer
# num_tokens
# emb_dim
# dim
# depth
# seq_len
# mem_len
# cmem_len
# reconstruction_loss_weight
# attn_dropout
# ff_dropout
# attn_layer_dropout
# gru_gated_residual
# mogrify_gru
# memory_layers
# one_head_kv
# ff_glu



class classifier(nn.Module):
    def __init__(self):
        # shard text encoder
        self.text_encoder = text_encoder
        # middle layer
        self.middle_layer = middleLayer()
        # output
    def forward(self):
        self.text_encoder
        self.middle_layer