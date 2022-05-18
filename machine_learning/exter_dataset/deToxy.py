from git import Repo
import os
url = "https://github.com/sreyan88/toxicity-detection-in-spoken-utterances"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'deToxy')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
