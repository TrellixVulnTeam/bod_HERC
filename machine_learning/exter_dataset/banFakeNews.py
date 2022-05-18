from git import Repo
import os
url = "https://www.kaggle.com/datasets/cryptexcode/banfakenews"

dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'banFakeNews')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
