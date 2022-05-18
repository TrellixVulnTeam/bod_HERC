import os
from git import Repo
url = "https://github.com/mohit3011/AbuseAnalyzer"
dir_fs = os.path.dirname(os.path.realpath(__file__))
Repo.clone_from(url,  os.path.join(dir_fs, 'abuseAnalyzer'))
