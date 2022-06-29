url = "https://github.com/qiangning/TORQUE-dataset"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import list_file, load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'TORQUE-dataset',url)


def get_data():
    path_train = get_path(dir_fs, 'TORQUE-dataset/data',"train.json")
    path_test = get_path(dir_fs, 'TORQUE-dataset/data',"test.json")
    path_dev = get_path(dir_fs, 'TORQUE-dataset/data',"dev.json")
    data = load_json(random.choice([path_train,path_test,path_dev]))
    key = random.choice(data.keys())
    passage = data[key]["passage"]
    question_answer_pairs = random.choice(data[key]["question_answer_pairs"].key())
    # todo the rest