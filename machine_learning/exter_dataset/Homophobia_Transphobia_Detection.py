url = "https://github.com/vitthal-bhandari/Homophobia-Transphobia-Detection"
import os
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

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
    eng_3_dev_tsv = TSV(eng_3_dev)
    eng_3_test_tsv = TSV(eng_3_test)
    eng_3_train_tsv = TSV(eng_3_train)
    eng_tam_3_dev_tsv = TSV(eng_tam_3_dev)
    eng_tam_3_train_tsv = TSV(eng_tam_3_train)
    eng_tam_3_test_tsv = TSV(eng_tam_3_test)
    tam_3_dev_tsv = TSV(tam_3_dev)
    tam_3_test_tsv = TSV(tam_3_test)
    tam_3_train_tsv = TSV(tam_3_train)
