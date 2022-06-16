import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/nguyenvo09/EMNLP2020"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'snopes',url)


def get_data():
    pass