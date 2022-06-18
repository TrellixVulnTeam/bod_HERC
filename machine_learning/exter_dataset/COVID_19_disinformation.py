url = "https://github.com/firojalam/COVID-19-disinformation"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'COVID-19-disinformation',url)



def get_data():
    pass