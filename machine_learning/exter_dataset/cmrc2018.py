import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV, load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/ymcui/cmrc2018"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'cmrc2018',url)

def get_data():
        paths = [
        get_path(dir_fs, 'cmrc2018',"data/cmrc2018_dev.json"),
        get_path(dir_fs, 'cmrc2018',"data/cmrc2018_train.json"),
        get_path(dir_fs, 'cmrc2018',"data/cmrc2018_trial.json")
        ]
        data = random.choice(load_json(paths))