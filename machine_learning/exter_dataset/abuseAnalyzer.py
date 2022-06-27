import os
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/mohit3011/AbuseAnalyzer"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'abuseAnalyzer',url)


def get_data():
    top_tweets = get_path(dir_fs, 'abuseAnalyzer',"AbuseAnalyzer_Dataset.tsv")
    data = TSV(top_tweets)