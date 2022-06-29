url = "https://github.com/rezacsedu/Bengali-Hate-Speech-Dataset"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Bengali-Hate-Speech-Dataset',url)



def get_data():
    bengali_hate = get_path(dir_fs, 'Bengali-Hate-Speech-Dataset',"data/")
    pass