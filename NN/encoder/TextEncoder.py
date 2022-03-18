
from tensorflow.keras import layers
#https://github.com/lucidrains/charformer-pytorch/blob/93752db1258e73c73a11bbffdf66eab87d3c3f07/charformer_pytorch/charformer_pytorch.py
class TextEncoder(layers.Layer):
    def __init__(self,num_tokens,dim,max_block_size = None,blocks = None,downsample_factor = 4,score_consensus_attn = True) -> None:
        pass
    def build(self, input_shape):
        pass
class TextDecoder(layers.Layer):
    def __init__(self,num_tokens,dim,) -> None:
        pass
    def build(self, input_shape):
        pass