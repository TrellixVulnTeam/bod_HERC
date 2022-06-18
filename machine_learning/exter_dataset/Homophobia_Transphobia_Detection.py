url = "https://github.com/vitthal-bhandari/Homophobia-Transphobia-Detection"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Homophobia-Transphobia-Detection',url)

def get_data():
    pass