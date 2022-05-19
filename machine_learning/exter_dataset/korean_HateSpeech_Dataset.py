import os
from git import Repo
url = "https://github.com/kocohub/korean-hate-speech"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'korean_HateSpeech_Dataset')
try:
    Repo.clone_from(url,  dir_fs)
except:
    pass
repo = Repo(dir_fs)
