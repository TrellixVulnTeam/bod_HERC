url = "https://github.com/victorknox/Hate-Speech-Detection-in-Hindi"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Hate-Speech-Detection-in-Hindi',url)



def get_data():
    pass