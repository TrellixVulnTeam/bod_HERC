url = "https://github.com/qiangning/TORQUE-dataset"
import os
from sysconfig import get_path
from machine_learning.exter_dataset.uitls.download import git_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'TORQUE-dataset',url)


def get_data():
    path ="able-Fact-Checking/data/all_csv"
    path = get_path(dir_fs, 'vaccineLies',path)