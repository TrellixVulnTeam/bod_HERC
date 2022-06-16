import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/germeval2021toxic/SharedTask/"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'SharedTask',url)


def get_data():
    pass