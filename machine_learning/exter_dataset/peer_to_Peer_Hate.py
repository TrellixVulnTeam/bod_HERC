import os
from git import Repo
url = "https://github.com/mayelsherif/hate_speech_icwsm18"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'peer_to_Peer_Hate')
try:
    Repo.clone_from(url,  dir_fs)
except:
    pass
repo = Repo(dir_fs)
