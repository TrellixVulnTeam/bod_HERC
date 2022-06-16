import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/gabll/some-like-it-hoax"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'some_Like_it_Hoax',url)


def get_data():
    pass
