
from machine_learning.exter_dataset.uitls.download import git_download
import os
url = "https://github.com/moinnadeem/stereoset.git"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'stereoSet',url)


def get_data():
    pass
