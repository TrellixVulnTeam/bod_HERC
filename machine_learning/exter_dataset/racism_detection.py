url = "https://github.com/angelamarpaung99/racism-detection"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'racism-detection',url)

def get_data():
    pass