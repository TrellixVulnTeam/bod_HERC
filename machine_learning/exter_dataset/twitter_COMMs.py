import os
import random
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/GiscardBiamby/Twitter-COMMs"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Twitter-COMMs',url)


def get_data():
    path ="data/tweets/twitter_comms_dataset.csv"
    path = get_path(dir_fs, 'vaccineLies',path)