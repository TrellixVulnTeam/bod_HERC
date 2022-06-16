import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/mayelsherif/hate_speech_icwsm18"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'peer_to_Peer_Hate',url)


def get_data():
    pass