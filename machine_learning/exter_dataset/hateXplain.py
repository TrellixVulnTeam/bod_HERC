from git import Repo
import os
url = "https://github.com/hate-alert/HateXplain"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'HateXplain')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
