import os
from git import Repo
url = "https://github.com/neemakot/Health-Fact-Checking"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'PUBHEALTH')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
