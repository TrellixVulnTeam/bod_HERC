import json
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/salesforce/DialFact"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'DialFact',url)



def get_data():
    valid_split = get_path(dir_fs, 'DialFact',"data/valid_split.jsonl")
    test_split = get_path(dir_fs, 'DialFact',"data/test_split.jsonl")
    path = random.choice([valid_split,test_split])
    data = random.choice(load_jsonl(path))
    context = random.choice(json.loads(data["context"]))
    data["response"]
    json.loads(data["evidence_list"])
    if data["type_label"] == "factual":
        pass
    elif data["type_label"] == "personal":
        pass
    if data["data_type"] == "generated":
        pass
    elif data["data_type"] == "written":
        pass
    if data["response_label"] == "NOT ENOUGH INFO":
        pass
    elif data["response_label"] == "SUPPORTS":
        pass
    elif data["response_label"] == "REFUTES":
        pass
    