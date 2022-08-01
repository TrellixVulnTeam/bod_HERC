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
        self.classifier = ClassifiesBinary(out_features =10)
        
        self.criterion = nn.CosineEmbeddingLoss()
    def hash_compare(self,hash):
        hash =hash [0]
        best = None
        best_value = 99999
        # print(hash2.shape)
        for data in self.datas:
            value = 0
            hash2 = self.hashing( data["value"],mode=data["mode"], **data["keywords"])
            print(hash2.shape)
            print(hash.shape)
            value = self.criterion(hash2, hash
                                   ,target=torch.tensor([1])).sum()
            print(value)
            if best_value> value:
                best = hash2
                best_value =   value
            # print(hash2 - hash )
        return best,best_value
    
    def hash_add(self,value,mode=None, **keywords):
        self.datas.append({"value":value, "mode":mode,"keywords":keywords})
        
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
        self.classifier = ClassifiesBinary(out_features =10)
        

    def forward(self, text,mode=None, **keywords):
        out, memories, aux_loss = self.encoder(text,mode=mode, **keywords)
        out, memories, aux_loss = self.trans(out, memories = memories)
        classifier = self.classifier(out)
        return classifier



class Retrieval(nn.Module):
    def __init__(self):
        super().__init__()
        self.trans_in = MiddleTransformer(emb_dim=variables.emb_dim, dim=variables.dim, depth=variables.depth, seq_len=variables.seq_len, mem_len=variables.mem_len, cmem_len=variables.cmem_len, reconstruction_loss_weight=variables.reconstruction_loss_weight,
                                            attn_dropout=variables.attn_dropout, ff_dropout=variables.ff_dropout, attn_layer_dropout=variables.attn_layer_dropout, gru_gated_residual=variables.gru_gated_residual, mogrify_gru=variables.mogrify_gru, memory_layers=variables.memory_layers, ff_glu=variables.ff_glu)
        self.classifier = ClassifiesBinary(out_features =5)

    def forward(self, x, memories = None,db = Memory_Handler()):
        t = x[0]
        x = self.trans_in(t,memories=memories)
        classifier = self.classifier(x)
        a = db.hash_compare(classifier)
        print(a)


