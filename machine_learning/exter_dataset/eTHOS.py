from git import Repo
import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset"

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Ethos',url)


def get_data():
    pass