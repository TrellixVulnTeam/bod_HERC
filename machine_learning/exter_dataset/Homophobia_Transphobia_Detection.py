url = "https://github.com/vitthal-bhandari/Homophobia-Transphobia-Detection"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.lalble_key import Hate, HateTargetClass

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Homophobia-Transphobia-Detection',url)

def get_data():
    eng_3_dev  = get_path(dir_fs, 'Homophobia-Transphobia-Detection',"Dataset/eng_3_dev.tsv")
    eng_3_test  = get_path(dir_fs, 'Homophobia-Transphobia-Detection',"Dataset/eng_3_test.tsv")
    eng_3_train  = get_path(dir_fs, 'Homophobia-Transphobia-Detection',"Dataset/eng_3_train.tsv")
    eng_tam_3_dev  = get_path(dir_fs, 'Homophobia-Transphobia-Detection',"Dataset/eng-tam_3_dev.tsv")
    eng_tam_3_train  = get_path(dir_fs, 'Homophobia-Transphobia-Detection',"Dataset/eng-tam_3_train.tsv")
    eng_tam_3_test  = get_path(dir_fs, 'Homophobia-Transphobia-Detection',"Dataset/eng_tam_3_test.tsv")
    tam_3_dev  = get_path(dir_fs, 'Homophobia-Transphobia-Detection',"Dataset/tam_3_dev.tsv")
    tam_3_test  = get_path(dir_fs, 'Homophobia-Transphobia-Detection',"Dataset/tam_3_test.tsv")
    tam_3_train  = get_path(dir_fs, 'Homophobia-Transphobia-Detection',"Dataset/tam_3_train.tsv")
    paths = [eng_3_dev,eng_3_test,eng_3_train,eng_tam_3_dev,eng_tam_3_train,eng_tam_3_test,tam_3_dev,tam_3_test,tam_3_train]
    path =random.choice(paths)
    eng_3_dev_tsv = TSV(path)
    if eng_3_dev_tsv["category"] == "Homophobic":
        Hate.Hate
        HateTargetClass.Homosexual
    elif eng_3_dev_tsv["category"] == "Transphobic":
        HateTargetClass.Transphobic
        Hate.Hate
    elif eng_3_dev_tsv["category"] == "Non-anti-LGBT+ content":
        Hate.NoHate
    eng_3_dev_tsv["text"]

