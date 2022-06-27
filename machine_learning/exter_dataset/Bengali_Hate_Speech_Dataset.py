url = "https://github.com/rezacsedu/Bengali-Hate-Speech-Dataset"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Bengali-Hate-Speech-Dataset',url)



def get_data():
    # TAB 
    bengali_hate_v1 = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/bengali_hate_v1.0.csv")
    bengali_hate_v2 = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/bengali_hate_v2.0.csv")
    path = random.choice([bengali_hate_v1,bengali_hate_v2])
    data = random.choice(CSV(path))