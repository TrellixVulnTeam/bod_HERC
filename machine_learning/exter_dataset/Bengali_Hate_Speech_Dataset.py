url = "https://github.com/rezacsedu/Bengali-Hate-Speech-Dataset"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Bengali-Hate-Speech-Dataset',url)



def get_data():
    bengali_hate1 = get_path(dir_fs, 'Bengali-Hate-Speech-Dataset',"bengali_hate_v1.0.csv")
    bengali_hate2 = get_path(dir_fs, 'Bengali-Hate-Speech-Dataset',"bengali_hate_v2.0.csv")
    path = random.choice([bengali_hate1,bengali_hate2])
    data_csv =  random.choice(CSV(path))
    data_csv["text"]
    data_csv["label"]
    data_csv["target"]