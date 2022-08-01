from transformers.models.bert.modeling_bert import BertModel
from transformers import BertTokenizer
import transformers
import torch
import torch.nn as nn

config = transformers.BertConfig()

class BERT_BD(nn.Module):
    def __init__(self):
        super(BERT_BD, self).__init__()
        self.bert = BertModel(config)
    def forward(self, inputs):
        x = self.bert(**inputs)
        return x
    
class memory_DB:
    def __init__(self):
        self.items =[]
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.bert1 = BertModel(config)
        self.bert2 = BertModel(config)
    
    def find(self,value):
        best_count = 0
        best_item = None
        for item in self.items:
            best_t = torch.abs(torch.sum(item["hash"] - value))
            if best_count > best_t:
                value = self.tokenizer(item["refs"], return_tensors="pt")
                best_item = self.bert2(**value)
        return best_item
    
    def add(self,text,refs,type="website",lang="UKN"):
        inputs = self.tokenizer(text, return_tensors="pt")
        hash = self.bert(**inputs)
        self.items.append({
            "hash":hash.pooler_output,
            "refs":refs,
            "type":type,
            "lang":lang
        })
        
class mongodb_DB:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.bert1 = BertModel(config)
        self.bert2 = BertModel(config)
    
    def find(self,value):
        pass
    
    def add(self,text,refs,type="website"):
        inputs = self.tokenizer(text, return_tensors="pt")
        hash = self.bert(**inputs)
        {
            "hash":hash.pooler_output,
            "refs":refs,
            "type":type
        }
