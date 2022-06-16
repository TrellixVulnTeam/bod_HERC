import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/kocohub/korean-hate-speech"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'korean_HateSpeech_Dataset',url)



def get_data():
    pass