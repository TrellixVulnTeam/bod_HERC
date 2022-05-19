import os
from git import Repo
url = "https://github.com/Supermaxman/covid19-vaccine-twitter"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'coVaxLies_v1')
try:
    Repo.clone_from(url,  dir_fs)
except:
    pass
repo = Repo(dir_fs)
