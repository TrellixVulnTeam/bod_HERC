import os
from machine_learning.exter_dataset.uitls.download import git_download

url = "https://archive.org/details/ECHR-ACL2019"
dir_fs = os.path.dirname(os.path.realpath(__file__))
# git_download(dir_fs, 'ECHR-ACL2019',url)