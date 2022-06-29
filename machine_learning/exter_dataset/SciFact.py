url = "https://scifact.s3-us-west-2.amazonaws.com/release/latest/data.tar.gz"
from cmath import e
import json
import random
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import file_download, gz_tar_download, zip_download
import os
from machine_learning.exter_dataset.uitls.get_path import get_path
try:
    dir_fs = os.path.dirname(os.path.realpath(__file__))
    gz_tar_download(dir_fs,"SciFact",url)
except:
    pass

def get_data():
    claims_dev = get_path(dir_fs, 'SciFact',"data/claims_dev.jsonl")
    claims_test = get_path(dir_fs, 'SciFact',"data/claims_test.jsonl")
    claims_train = get_path(dir_fs, 'SciFact',"data/claims_train.jsonl")
    path2 = get_path(dir_fs, 'SciFact',"data/corpus.jsonl")
    data = random.choice(load_jsonl(random.choice([claims_dev,claims_test,claims_train])))
    data["claim"]
    crops =[]
    evidence = data["evidence"]
    for id in evidence.keys():
        title = None
        abstract = None
        structured = None
        for i_data in load_jsonl(path2):
                if i_data["id"] == id:
                    title = i_data["title"]
                    abstract = i_data["abstract"]
                    structured = i_data["structured"]              
        if evidence[id]["label"] == "SUPPORT":
            crops.append({
                "title":title,
                "abstract":abstract,
                "structured":structured
            })
        elif evidence[id]["label"] == "CONTRADICT":
            crops.append({
                "title":title,
                "abstract":abstract,
                "structured":structured
            })
            pass
        evidence[id]
        pass