import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV, load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/hate-alert/HateXplain"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'HateXplain',url)


def get_data():
    test_dataset = get_path(dir_fs, 'HateXplain',"dataset.json")
    data = random.choice(load_json(test_dataset))