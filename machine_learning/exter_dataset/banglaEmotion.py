from git import Repo
import os
url = "https://data.mendeley.com/datasets/24xd7w7dhp/1"
# lang = ""

dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'banglaEmotion')
try:
    Repo.clone_from(url,  dir_fs)
except:
    pass
repo = Repo(dir_fs)
