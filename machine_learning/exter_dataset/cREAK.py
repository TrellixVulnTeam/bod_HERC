import os
import random
from sysconfig import get_path
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.service_scrap.modules.retrieval import Memory_Handler
dir_fs = os.path.dirname(os.path.realpath(__file__))
url = "https://github.com/yasumasaonoe/creak"
git_download(dir_fs, 'creak',url)


def get_data():
    db = Memory_Handler()
    path = [get_path(dir_fs, 'creak',"data/dev.json"),get_path(dir_fs, 'creak',"data/train.json")]
    data = load_jsonl(random.choice(path))
    data = random.choice(data)
    if data["label"] == "false":
        pass
    else:
        pass
    data["entity"] 
    data["sentence"] 
    data["explanation"] 
    data["en_wiki_pageid"] 