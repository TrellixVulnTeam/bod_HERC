
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
import os
url = "https://github.com/moinnadeem/stereoset.git"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'stereoSet',url)


def get_data():
    path = get_path(dir_fs, 'stereoSet',"data/dev.json")
    data = load_json(path)
    data = random.choice(data["data"]["intersentence"])
    data["target"]
    data["bias_type"]
    data["context"]
    for sentence in data["sentences"]:
        pass