from git import Repo
import os
url = "https://github.com/dD2405/Twitter_Sentiment_Analysis"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'Twitter_Sentiment_Analysis')
try:
    Repo.clone_from(url,  dir_fs)
except:
    pass
repo = Repo(dir_fs)
