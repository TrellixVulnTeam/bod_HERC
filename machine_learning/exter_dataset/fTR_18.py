import os
from git import Repo
url = "https://github.com/dcaled/FTR-18"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'FTR-18')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
