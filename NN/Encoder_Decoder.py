import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers



class Encoder_Decoder_tree:
    def  __init__(self) -> None:
        layers.Embedding(1000, 64, input_length=10)
