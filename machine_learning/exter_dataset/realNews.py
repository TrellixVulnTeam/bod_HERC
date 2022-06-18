import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/rowanz/grover/"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'grover',url)




def get_data():
    pass