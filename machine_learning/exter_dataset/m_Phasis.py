import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/uds-lsv/mphasis"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'mphasis',url)

def get_data():
    covmis_stance = get_path(dir_fs, 'mphasis',"covmis_stance.csv")
    de_test = get_path(dir_fs, 'mphasis',"de.test.csv")
    de_test_normal = get_path(dir_fs, 'mphasis',"de.test.normal.csv")
    de_train_fringe = get_path(dir_fs, 'mphasis',"de.train.fringe.csv")
    de_valid = get_path(dir_fs, 'mphasis',"de.valid.csv")
    de_valid_normal = get_path(dir_fs, 'mphasis',"de.valid.normal.csv")
    fr_test_fringe = get_path(dir_fs, 'mphasis',"fr.test.fringe.csv")
    fr_train = get_path(dir_fs, 'mphasis',"fr.train.csv")
    fr_train_normal = get_path(dir_fs, 'mphasis',"fr.train.normal.csv")
    fr_valid_fringe = get_path(dir_fs, 'mphasis',"fr.valid.fringe.csv")
    de_test_fringe = get_path(dir_fs, 'mphasis',"de.test.fringe.csv")
    de_train = get_path(dir_fs, 'mphasis',"de.train.csv")
    de_train_normal = get_path(dir_fs, 'mphasis',"de.train.normal.csv")
    de_valid_fringe = get_path(dir_fs, 'mphasis',"de.valid.fringe.csv")
    fr_test = get_path(dir_fs, 'mphasis',"fr.test.csv")
    fr_test_normal = get_path(dir_fs, 'mphasis',"fr.test.normal.csv")
    fr_train_fringe = get_path(dir_fs, 'mphasis',"fr.train.fringe.csv")
    fr_valid = get_path(dir_fs, 'mphasis',"fr.valid.csv")
    fr_valid_normal = get_path(dir_fs, 'mphasis',"fr.valid.normal.csv")
    paths = [covmis_stance,de_test,de_test_normal,de_train_fringe,de_valid,de_valid_normal,fr_test_fringe,fr_train,fr_train_normal,fr_valid_fringe,de_test_fringe,de_train,de_train_normal,de_valid_fringe,fr_test,fr_test_normal,fr_train_fringe,fr_valid,fr_valid_normal]
    path = random.choice(paths)
    data = random.choice(CSV(path))
