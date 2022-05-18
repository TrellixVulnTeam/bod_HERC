import os
from git import Repo
url = "https://github.com/g-luo/news_clippings"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'news_clippings')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
