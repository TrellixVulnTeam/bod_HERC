url = "https://github.com/safe-graph/GNN-FakeNews"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'GNN-FakeNews',url)


def get_data():
    path_dev = get_path(dir_fs, 'TORQUE-dataset',"data/dev.json")
    path_test = get_path(dir_fs, 'TORQUE-dataset',"data/test.json")
    path_train = get_path(dir_fs, 'TORQUE-dataset',"data/train.json")
    p = random.choice([path_dev,path_test,path_train])
    data = load_json(p)
    key = random.choice(data.keys())
    data[key]["passage"]
    data[key]["question_answer_pairs"]
    data[key]["passage"]