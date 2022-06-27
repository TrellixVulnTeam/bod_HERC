import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/salesforce/DialFact"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'DialFact',url)



def get_data():
    valid_split = get_path(dir_fs, 'DialFact',"valid_split.jsonl")
    test_split = get_path(dir_fs, 'DialFact',"test_split.jsonl")
    path = random.choice([valid_split,test_split])
    data = random.choice(load_jsonl(path))
    