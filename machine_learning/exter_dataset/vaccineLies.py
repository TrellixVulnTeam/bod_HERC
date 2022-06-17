url = "https://github.com/Supermaxman/vaccine-lies"
import os
import random
from sysconfig import get_path
from machine_learning.exter_dataset.uitls.decode_data import load_json, load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'vaccineLies',url)



def get_data():
    paths = []
    paths.append("vaccineLies/covid19/annotations/dev.jsonl")
    paths.append("vaccineLies/covid19/annotations/dev.jsonl")
    paths.append("vaccineLies/covid19/annotations/dev.jsonl")
    path = get_path(dir_fs, 'vaccineLies',random.choice(paths))
    c = load_jsonl(path)