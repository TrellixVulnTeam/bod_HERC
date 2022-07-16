import torch
import torch.nn as nn
from machine_learning.service_scrap.modules.pooler import Classifies, ClassifiesBinary, Pooler
import machine_learning.service_scrap.modules.variables as variables
from machine_learning.service_scrap.modules.compressive_transformer_pytorch import CompressiveTransformer ,MiddleTransformer
from machine_learning.service_scrap.modules.mode_box import ModeBox
import pymongo

def DB_loader():
    pass


class DB_Handler:
    def __init__(self):
        pass
    def hash_compare(hash):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydatabase"]
        mycol = mydb["customers"]
        values = []
        for count, item in enumerate(hash):
            value = {"$subtract": [item, "$hash."+str(count)]}
            values.append(value)
        data = {{"finalTotal": {"$add": values}}}
        result = mycol.find(data).sort("finalTotal", -1).limit(5)
        return result

    def hash_add(hash,data):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydatabase"]
        mycol = mydb["customers"]
        mycol.insert_one({"hash":hash, "data":data})

    def hash_del(data):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["mydatabase"]
        mycol = mydb["customers"]
        mycol.delete_one(data)
        

class Memory_Handler:
    def __init__(self):
        self.datas = []
        self.hashing = Hashing()
        
    def hash_compare(self,hash):
        best = None
        best_value = None
        for data in self.datas:
            value = 0
            for count, value in enumerate(data["hash"][0]):
               value = hash[0][count] + value
        
        return best,best_value
    
    def hash_add(self,value,type,where=None,mode=None, **keywords):
        hash = self.hashing(self, value,mode=mode, **keywords)
        self.datas.append({"type":type, "hash":hash, "value":value, "keywords":keywords})
        
    def hash_del(self,data):
        pass
    
    def reset(self):
        self.datas = []

class Hashing(nn.Module):
    def __init__(self):
        super().__init__()
        self.trans = MiddleTransformer(emb_dim=variables.emb_dim, dim=variables.dim, depth=variables.depth, seq_len=variables.seq_len, mem_len=variables.mem_len, cmem_len=variables.cmem_len, reconstruction_loss_weight=variables.reconstruction_loss_weight,
                                            attn_dropout=variables.attn_dropout, ff_dropout=variables.ff_dropout, attn_layer_dropout=variables.attn_layer_dropout, gru_gated_residual=variables.gru_gated_residual, mogrify_gru=variables.mogrify_gru, memory_layers=variables.memory_layers, ff_glu=variables.ff_glu)
        self.encoder = ModeBox()
        self.classifier = ClassifiesBinary(out_features =255)
        

    def forward(self, text,mode=None, **keywords):
        out, memories, aux_loss = self.encoder(text,mode=mode, **keywords)
        out, memories, aux_loss = self.trans(out, memories = memories)
        classifier = self.classifier(out)
        return classifier


class ffff:
    def __init__(self):
        pass
    def forward(self):
        torch.numel(a)



class Retrieval(nn.Module):
    def __init__(self):
        super().__init__()
        self.trans_in = MiddleTransformer(emb_dim=variables.emb_dim, dim=variables.dim, depth=variables.depth, seq_len=variables.seq_len, mem_len=variables.mem_len, cmem_len=variables.cmem_len, reconstruction_loss_weight=variables.reconstruction_loss_weight,
                                            attn_dropout=variables.attn_dropout, ff_dropout=variables.ff_dropout, attn_layer_dropout=variables.attn_layer_dropout, gru_gated_residual=variables.gru_gated_residual, mogrify_gru=variables.mogrify_gru, memory_layers=variables.memory_layers, ff_glu=variables.ff_glu)
        self.encoder = ModeBox()
        self.classifier = ClassifiesBinary(out_features =255)

    def forward(self, x, memories = None,db = Memory_Handler()):
        loss = None
        x = self.trans_in(x)
        classifier = self.classifier(x)
        data = db.hash_compare(classifier)
        if data["type"] == "TEXT":
            pass
        elif data["type"] == "URL":
            pass
        print(data)
        return x , loss


