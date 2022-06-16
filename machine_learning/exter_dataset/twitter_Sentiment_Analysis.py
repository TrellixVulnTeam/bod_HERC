import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/dD2405/Twitter_Sentiment_Analysis"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Twitter_Sentiment_Analysis',url)


def get_data():
    pass