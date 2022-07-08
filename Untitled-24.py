
import torch
from machine_learning.exter_dataset.uitls.v import NN_Plain_Text, NN_PlainTextConfig

config = NN_PlainTextConfig()
tokenizer = NN_Plain_Text(config)

tensor_text = "hello"
mask = torch.ones(1, len(tensor_text)).bool()
# (1, 256, 512), (1, 256)
tokens, mask, c = tokenizer(tensor_text, "Text", "en", mask)
print(tokens)
print(c)