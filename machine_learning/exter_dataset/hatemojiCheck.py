import os
from git import Repo
url = "https://github.com/HannahKirk/Hatemoji"

dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'Hatemoji')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
