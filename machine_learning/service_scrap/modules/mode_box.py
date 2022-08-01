import torch
import torch.nn as nn
from machine_learning.service_scrap.modules.text import text_encoder
import machine_learning.service_scrap.modules.variables as variables

class ModeBox(nn.Module):
    def __init__(self):
        super().__init__()
        pass
    def forward(self,x,mode="TEXT",**keywords):
        if mode == "TEXT":
            d = modes[mode](x,**keywords)
        return d

modes = {
    "TEXT":text_encoder,
}
