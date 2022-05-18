from git import Repo
import os
url = "https://github.com/FakeNewsChallenge/fnc-1"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'fnc-1')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
