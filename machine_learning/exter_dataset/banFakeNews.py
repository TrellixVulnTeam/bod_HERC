import os
from kaggle.api.kaggle_api_extended import KaggleApi
from machine_learning.exter_dataset.uitls.decode_data import CSV

from machine_learning.exter_dataset.uitls.get_path import get_path
name = "cryptexcode/banfakenews"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs,"repo", 'banFakeNews')
try:
    os.mkdir(dir_fs)
except:
    pass
api = KaggleApi()
api.authenticate()
api.dataset_download_files(name,path=dir_fs, unzip=True)
import random

def get_data():
    c = random.randint(0,4)
    if c == 0:
        Authentic = get_path(dir_fs, 'banFakeNews',"Authentic-48K.csv")
        data = random.choice(CSV(Authentic))
        if data["category"] == "International":
            pass
        if data["category"] == "Miscellaneous":
            pass
        if data["category"] == "Sports":
            pass
        if data["category"] == "Lifestyle":
            pass
        if data["category"] == "Politics":
            pass
        if data["category"] == "Technology":
            pass
        if data["category"] == "National":
            pass
        if data["category"] == "Politics":
            pass
        if data["category"] == "Entertainment":
            pass
        if data["category"] == "Finance":
            pass
        if data["category"] == "Crime":
            pass
        if data["category"] == "Crime":
            pass
        if data["category"] == "Education":
            pass
        # tokens, mask, c = tokenizer(data["content"] , "Text", "unknown", None)
        # tokens, mask, c = tokenizer(data["headline"] , "Text", "unknown", None)
        data["domain"]
    elif c == 1:
        Authentic = get_path(dir_fs, 'banFakeNews',"Authentic-48K.csv")
        data = random.choice(CSV(Authentic))
        if data["category"] == "International":
            # International
            pass
        elif data["category"] == "Miscellaneous":
            # Miscellaneous
            pass
        elif data["category"] == "Sports":
            # Sports
            pass
        elif data["category"] == "Lifestyle":
            # Lifestyle
            pass
        elif data["category"] == "Politics":
            # Politics
            pass
        elif data["category"] == "Technology":
            # Technology
            pass
        elif data["category"] == "National":
            # National
            pass
        
        if data["category"] == "Entertainment":
            pass
        elif data["category"] == "Finance":
            pass
        elif data["category"] == "Crime":
            pass
        elif data["category"] == "Crime":
            pass
        if data["category"] == "Education":
            pass
        
        if data["relation"] == "Related":
            pass
        elif data["relation"] == "Unrelated":
            pass
        data["domain"] 
        data["source"]
        # tokens, mask, c = tokenizer(data["content"] , "Text", "unknown", None)
        # tokens, mask, c = tokenizer(data["headline"] , "Text", "unknown", None)
    elif c == 2:
        LabeledFake = get_path(dir_fs, 'banFakeNews',"LabeledFake-1K.csv")
        data = random.choice(CSV(LabeledFake))
        if data["category"] == "International":
            pass
        elif data["category"] == "Miscellaneous":
            pass
        elif data["category"] == "Sports":
            pass
        elif data["category"] == "Lifestyle":
            pass
        elif data["category"] == "Politics":
            pass
        elif data["category"] == "Technology":
            pass
        elif data["category"] == "National":
            pass
        elif data["category"] == "Politics":
            pass
        
        if data["category"] == "Entertainment":
            pass
        elif data["category"] == "Finance":
            pass
        elif data["category"] == "Crime":
            pass
        elif data["category"] == "Crime":
            pass
        if data["category"] == "Education":
            pass
        
        if data["relation"] == "Related":
            pass
        elif data["relation"] == "Unrelated":
            pass
        
        if data["F-type"] == "Satire":
            pass
        elif data["F-type"] == "Clickbaits":
            pass
        elif data["F-type"] == "Fake":
            pass
        data["headline"]
        
        # tokens, mask, c = tokenizer(data["content"] , "Text", "unknown", None)
        # tokens, mask, c = tokenizer(data["headline"] , "Text", "unknown", None)
        data["domain"]
    elif c == 3:
        LabeledAuthentic = get_path(dir_fs, 'banFakeNews',"LabeledAuthentic-7K.csv")
        data = random.choice(CSV(LabeledAuthentic))
        if data["category"] == "International":
            pass
        elif data["category"] == "Miscellaneous":
            pass
        elif data["category"] == "Sports":
            pass
        elif data["category"] == "Lifestyle":
            pass
        elif data["category"] == "Politics":
            pass
        elif data["category"] == "Technology":
            pass
        elif data["category"] == "National":
            pass
        elif data["category"] == "Politics":
            pass
        
        if data["category"] == "Entertainment":
            pass
        elif data["category"] == "Finance":
            pass
        elif data["category"] == "Crime":
            pass
        elif data["category"] == "Crime":
            pass
        if data["category"] == "Education":
            pass
        # tokens, mask, c = tokenizer(data["content"] , "Text", "unknown", None)
        # tokens, mask, c = tokenizer(data["headline"] , "Text", "unknown", None)
        data["domain"]
    elif c== 4:
        Fake = get_path(dir_fs, 'banFakeNews',"Fake-1K.csv")
        data = random.choice(CSV(Fake))
        if data["category"] == "International":
            pass
        elif data["category"] == "Miscellaneous":
            pass
        elif data["category"] == "Sports":
            pass
        elif data["category"] == "Lifestyle":
            pass
        elif data["category"] == "Politics":
            pass
        elif data["category"] == "Technology":
            pass
        elif data["category"] == "National":
            pass
        elif data["category"] == "Politics":
            pass
        # tokens, mask, c = tokenizer(data["content"] , "Text", "unknown", None)
        # tokens, mask, c = tokenizer(data["headline"] , "Text", "unknown", None)
        data["domain"]