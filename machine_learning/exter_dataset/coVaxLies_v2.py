from git import Repo
import os
url = "https://github.com/Supermaxman/vaccine-lies/tree/master/covid19"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'coVaxLies_v2')
try:
    Repo.clone_from(url,  dir_fs)
except:
    pass
repo = Repo(dir_fs)
