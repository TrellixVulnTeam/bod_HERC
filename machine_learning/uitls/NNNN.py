import torch
import torch.nn as nn
from machine_learning.uitls.TransformerModel import TransformerModel, TransformerEncoderLayer, TransformerEncoder


class brain_box(nn.Module):
    def __init__(self, out_features, in_features, dropout=0.5):
        super().__init__()
        self.out_features = out_features
        self.transformer_encoder = nn.Linear(in_features, out_features)

    def forward(self, src, mask):
        print(src[0][0].size())
        return (self.transformer_encoder(src[0][0]))


class training_block(nn.Module):
    def __init__(self, ntokens, emsize, nhead, d_hid, nlayers, dropout):
        super().__init__()
        self.ntokens = ntokens
        self.model = TransformerModel(
            ntokens, emsize, nhead, d_hid, nlayers, dropout)
        self.outputs = {}

    def forward(self, src, mask):
        output = {}
        output, src_mask = self.model(src, src_mask=mask)
        for name in self.outputs.keys():
            output[name] = self.outputs[name]['output'](output, src_mask)
        return output

    def train(self, basepairs, mask, targets):
        # make  sure we have all the Lables
        for name in targets.keys():
            if name not in self.outputs:
                self.outputs[name] = {"label": []}
            for name_lib in targets[name]:
                if name_lib not in self.outputs[name]["label"]:
                    self.outputs[name]["label"].append(name_lib)
                    size = len(self.outputs[name]["label"])
                    if "output" not in self.outputs[name].keys():
                        self.outputs[name]["output"] = brain_box(
                            size, self.ntokens)
                    if size != self.outputs[name]["output"].out_features:
                        self.outputs[name]["output"] = brain_box(
                            size, self.ntokens)
                        pass
        # do that modle thing
        output, src_mask = self.model(basepairs, src_mask=mask)
        for name in targets.keys():
            size = len(self.outputs[name]['label'])
            a_out = [0] * size
            for ii in targets[name]:
                index = self.outputs[name]['label'].index(ii)
                a_out[index] = 1
            print(output[0].size())
            xx = self.outputs[name]['output'](output, src_mask)
            print(xx)
