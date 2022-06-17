import os
from machine_learning.exter_dataset.uitls.download import git_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
url = "https://github.com/cuilimeng/CoAID"
git_download(dir_fs, 'CoAID',url)


def get_data():
    pass