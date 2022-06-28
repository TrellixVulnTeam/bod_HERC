import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/marshallwhiteorg/emnlp19-media-bias"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'emnlp19-media-bias',url)


def get_data():
    r1_training_all = get_path(dir_fs, 'Table-Fact-Checking',"collected_data/r1_training_all.json")
    r2_training_all = get_path(dir_fs, 'Table-Fact-Checking',"collected_data/r2_training_all.json")
    path = random.choice([r1_training_all,r2_training_all])
    data = load_json(path)
    key = random.choice(data.keys())
    path = get_path(dir_fs, 'Table-Fact-Checking',"data/all_csv/"+key)
    data_csv = CSV(path,delimiter="#")
    size = len(data[key][0])
    index = random.randint(0,size)
    data[key][0][index]
    if data[key][1][index] == 0:
        # False
        pass
    elif data[key][1][index] == 1:
        # True
        pass
    data[key][2]