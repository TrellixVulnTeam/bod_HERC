from git import Repo
import os
url = "https://github.com/HKUST-KnowComp/MLMA_hate_speech"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'mLMA_Hate_Speech')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
