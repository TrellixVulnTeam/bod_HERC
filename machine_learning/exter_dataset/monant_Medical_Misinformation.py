import os
from git import Repo
url = "https://github.com/kinit-sk/medical-misinformation-dataset"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'monant_Medical_Misinformation')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
