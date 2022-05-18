import os
from git import Repo
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'CoAID')
url = "https://github.com/JerryWei03/COVID-Q"
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
