import os
from sysconfig import get_path
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/JAugusto97/ToLD-Br"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ToLD-Br',url)


def get_data():
    path = get_path(dir_fs, 'ToLD-Br',"ToLD-BR.csv")