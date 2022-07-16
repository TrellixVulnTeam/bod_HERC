from machine_learning.service_scrap.modules.compressive_transformer_pytorch import CompressiveTransformer
import machine_learning.service_scrap.modules.variables as variables

middleLayer = lambda : CompressiveTransformer(
    num_tokens = variables.dim,
    seq_len = variables.seq_len,
    depth = variables.depth,
    emb_dim = variables.emb_dim,
    memory_layers = variables.memory_layers,
    mem_len = variables.mem_len,
    cmem_len = variables.cmem_len,
    gru_gated_residual = variables.gru_gated_residual,
    mogrify_gru = variables.mogrify_gru,
    attn_dropout = variables.attn_dropout,
    ff_glu = variables.ff_glu,
    ff_dropout = variables.ff_dropout,
    attn_layer_dropout = variables.attn_layer_dropout,
    reconstruction_loss_weight = variables.reconstruction_loss_weight
    )