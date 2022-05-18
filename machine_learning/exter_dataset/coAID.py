from git import Repo
import os
url = "https://github.com/cuilimeng/CoAID"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'CoAID')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
