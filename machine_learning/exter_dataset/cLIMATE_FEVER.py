import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/tdiggelm/climate-fever-dataset"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'climate-fever',url)


def get_data():
    climate_fever = get_path(dir_fs, 'climate-fever', "dataset/climate-fever.jsonl")
    data = random.choice(load_jsonl(climate_fever))