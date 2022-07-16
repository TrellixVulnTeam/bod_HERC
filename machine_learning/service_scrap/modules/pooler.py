import torch
import torch.nn.functional as functional
import torch.nn as nn
import machine_learning.service_scrap.modules.variables as variables

class Pooler(nn.Module):
    def __init__(self, hidden_size = variables.emb_dim):
        super().__init__()
        self.dense = nn.Linear(hidden_size, hidden_size)
        self.activation = nn.Sigmoid()

    def forward(self, hidden_states: torch.Tensor):
        first_token_tensor = hidden_states[0][:, 0]
        pooled_output = self.dense(first_token_tensor)
        return self.activation(pooled_output)



class Classifies(nn.Module):
    def __init__(self, hidden_size = variables.emb_dim,out_features = variables.emb_dim):
        super().__init__()
        self.dense = nn.Linear(hidden_size, out_features)
        self.activation = nn.Sigmoid()

    def forward(self, hidden_states: torch.Tensor):
        first_token_tensor = hidden_states[0][:, 0]
        pooled_output = self.dense(first_token_tensor)
        return  self.activation(pooled_output)



class ClassifiesBinary(nn.Module):
    def __init__(self, hidden_size = variables.dim ,out_features = variables.emb_dim):
        super().__init__()
        self.dense = nn.Linear(hidden_size, out_features)
        self.activation = nn.Sigmoid()

    def forward(self, hidden_states: torch.Tensor):
        first_token_tensor = hidden_states[0]
        pooled_output = self.dense(first_token_tensor)
        return self.activation(pooled_output)  