import os
from git import Repo
url = "https://github.com/Supermaxman/covid19-vaccine-twitter"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'coVaxLies_v1')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
