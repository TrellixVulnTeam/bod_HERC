
import os
import machine_learning.exter_data
from machine_learning.uitls.NNNN import training_block
from machine_learning.uitls.TransformerModel import TransformerModel
import asyncio
from torch.utils.data import Dataset, DataLoader
from machine_learning.service_scrap.service import Getdata
import torch

# char_l = 256
# # tokenizer = GBST(
# #     num_tokens=256,
# #     dim=512,
# #     max_block_size=4,
# #     downsample_factor=4,
# #     score_consensus_attn=True
# # )

# ntokens = 256  # size of vocabulary
# emsize = 512  # embedding dimension
# d_hid = 200  # dimension of the feedforward network model in nn.TransformerEncoder
# nlayers = 2  # number of nn.TransformerEncoderLayer in nn.TransformerEncoder
# nhead = 2  # number of heads in nn.MultiheadAttention
# dropout = 0.2  # dropout probability
# model = training_block(ntokens, emsize, nhead, d_hid, nlayers, dropout)


# def text_embedding(text):
#     bits_char = []
#     for i in bytearray(text, 'utf-8'):
#         bits_char.append(i)
#     count = len(bits_char)
#     mask = torch.ones(1, count).bool()
#     basepairs = torch.tensor([bits_char])
#     return mask, basepairs


async def NN_main(name):
    pass
    # async for data in Getdata():
    #     if len(data[2]) < 40167:
    #         pass
            
    #         mask, basepairs = text_embedding(data[2])
    #         output = model.train(basepairs, mask, data[0])



