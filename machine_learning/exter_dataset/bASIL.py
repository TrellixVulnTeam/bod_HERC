from git import Repo
import os
url = "https://github.com/marshallwhiteorg/emnlp19-media-bias"

dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'BASIL')
try:
    Repo.clone_from(url,  dir_fs)
except:
    pass
repo = Repo(dir_fs)
