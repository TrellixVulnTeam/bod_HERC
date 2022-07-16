import json
import os
import random
from machine_learning.data_url import load_url
from machine_learning.exter_dataset.uitls.decode_data import CSV, load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.service_scrap.modules.retrieval import Memory_Handler
url = "https://github.com/salesforce/DialFact"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'DialFact',url)



def get_data():
    db = Memory_Handler()
    valid_split = get_path(dir_fs, 'DialFact',"data/valid_split.jsonl")
    test_split = get_path(dir_fs, 'DialFact',"data/test_split.jsonl")
    path = random.choice([valid_split,test_split])
    data = random.choice(load_jsonl(path))
    for context in data["context"]:
        pass
    data["response"]
    data["data_type"]
    for evidence in data["evidence_list"]:
        title = evidence[0]
        text = load_url(evidence[1])
        evidence = evidence[2]
        
    
    data["response_label"]
    data["type_label"]