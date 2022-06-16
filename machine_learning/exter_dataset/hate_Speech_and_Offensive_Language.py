import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/t-davidson/hate-speech-and-offensive-language"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate_Speech_and_Offensive_Language',url)


def get_data():
    pass