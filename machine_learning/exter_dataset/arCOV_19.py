import os
import random
from machine_learning.exter_dataset.uitls.decode_data import list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://gitlab.com/bigirqu/ArCOV-19"

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ArCOV-19',url)


def get_data():
    all_tweets = get_path(dir_fs, 'ArCOV-19',"dataset/all_tweets")
    top_tweets = get_path(dir_fs, 'ArCOV-19',"dataset/top_tweets")
    path = list_file(random.choice([all_tweets,top_tweets]))
    