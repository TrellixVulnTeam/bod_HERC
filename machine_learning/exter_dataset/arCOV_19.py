import os
from git import Repo
url = "https://gitlab.com/bigirqu/ArCOV-19"

dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'ArCOV-19')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
