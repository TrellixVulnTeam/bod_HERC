import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/MELALab/nela-gt"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'nELA_GT_2020',url)
## https://dataverse.harvard.edu/file.xhtml?fileId=4417502&version=2.0


def get_data():
    path_conservative = get_path(dir_fs, 'nELA_GT_2020',"conservative.txt")