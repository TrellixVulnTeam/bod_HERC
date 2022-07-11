import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://doi.org/10.5281/zenodo.1181813"
dir_fs = os.path.dirname(os.path.realpath(__file__))
# git_download(dir_fs, 'buzzfeed-webis-fake-news-16',url)



def get_data():
    pass