url = "https://github.com/qiangning/TORQUE-dataset"
import os
from machine_learning.exter_dataset.uitls.decode_data import list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'TORQUE-dataset',url)


def get_data():
        pass