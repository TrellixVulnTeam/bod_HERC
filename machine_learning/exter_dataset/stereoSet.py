
import random
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
import os
url = "https://github.com/moinnadeem/stereoset.git"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'stereoSet',url)


def get_data():
    path = get_path(dir_fs, 'stereoset',"data/dev.json")