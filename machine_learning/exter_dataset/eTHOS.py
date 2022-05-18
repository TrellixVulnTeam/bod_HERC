from git import Repo
import os
url = "https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset"

dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'Ethos')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
