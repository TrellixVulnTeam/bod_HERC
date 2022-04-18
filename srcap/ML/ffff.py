import torch
from transformers import BertTokenizer
from transformers import BertConfig, BertModel
from ML.Layer.transformer import Model
config = BertConfig()
model = Model(config)
tokens = torch.randint(0, 257, (1, 1023))  # uneven number of tokens (1023)
mask = torch.ones(1, 1023).bool()
print(model(tokens, attention_mask=mask))
