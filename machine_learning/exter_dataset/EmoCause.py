import os
from git import Repo
from machine_learning.exter_dataset.uitls.download import git_download

url = "https://github.com/skywalker023/focused-empathy"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'EmoCause',url)


def get_data():
    pass