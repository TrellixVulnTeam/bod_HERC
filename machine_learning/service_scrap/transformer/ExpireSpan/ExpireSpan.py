import math
import torch
from torch import nn, einsum
import torch.nn.functional as F
from einops import rearrange, repeat



class ExpireSpan(nn.Module):
    def __init__(self, dim, max_mem_len, ramp_length):
        super().__init__()
        self.max_mem_len = max_mem_len
        self.ramp_length = ramp_length
        self.to_expiration = nn.Linear(dim, 1)
        nn.init.constant_(self.to_expiration.bias.data, val = -self.max_mem_len)

    def forward(self, mem, time, seq_len):
        exps = self.to_expiration(mem).squeeze(-1).sigmoid() * self.max_mem_len
        exps = rearrange(exps, 'b j -> b () () j')
        t = rearrange(time, 'b j -> b () () j')
        r = F.pad(exps - t, (0, seq_len), value = 1.)
        mask = torch.clamp((r / self.ramp_length) + 1, min = 0., max = 1.)
        return exps, mask