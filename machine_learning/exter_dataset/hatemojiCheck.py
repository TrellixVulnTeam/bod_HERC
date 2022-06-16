import os
from machine_learning.exter_dataset.uitls.download import git_download

url = "https://github.com/HannahKirk/Hatemoji"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Hatemoji',url)


def get_data():
    pass