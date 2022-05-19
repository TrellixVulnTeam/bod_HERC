from git import Repo
import os
url = "https://github.com/snigdhac/StoryComprehension_EMNLP"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'rOCStories')
try:
    Repo.clone_from(url,  dir_fs)
except:
    pass
repo = Repo(dir_fs)
