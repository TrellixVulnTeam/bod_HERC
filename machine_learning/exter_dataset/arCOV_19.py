import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://gitlab.com/bigirqu/ArCOV-19"

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ArCOV-19',url)


def get_data():
    pass