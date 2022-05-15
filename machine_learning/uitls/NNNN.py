import torch
from charformer_pytorch import GBST

tokenizer = GBST(num_tokens=257, dim=512, max_block_size=4,
                 downsample_factor=4, score_consensus_attn=True)

tokens = torch.randint(0, 257, (1, 1023))  # uneven number of tokens (1023)
mask = torch.ones(1, 1023).bool()

# both tokens and mask will be appropriately downsampled

tokens, mask = tokenizer(tokens, mask=mask)  # (1, 256, 512), (1, 256)
print(tokens[0])
