import os
from git import Repo
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'creak')
url = "https://github.com/yasumasaonoe/creak"
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
