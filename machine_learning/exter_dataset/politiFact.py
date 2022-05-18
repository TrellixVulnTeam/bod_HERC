from git import Repo
import os
url = "https://github.com/nguyenvo09/EMNLP2020"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'EMNLP2020')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
