import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/sociocom/covid19_dataset"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'covid19_dataset',url)



def get_data():
    pass