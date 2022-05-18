from git import Repo
import os
url = "https://github.com/t-davidson/hate-speech-and-offensive-language"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'hate_Speech_and_Offensive_Language')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
