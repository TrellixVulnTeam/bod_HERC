import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/uds-lsv/mphasis"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'fnc-1')
git_download(dir_fs, 'mphasis',url)

def get_data():
    pass