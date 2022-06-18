url = "https://github.com/GloriaComandini/Corpora"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Corpora',url)



def get_data():
    pass