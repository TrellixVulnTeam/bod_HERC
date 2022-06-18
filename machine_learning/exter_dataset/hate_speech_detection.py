url = "https://github.com/faisalisafk/hate_speech_detection"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate_speech_detection',url)



def get_data():
    pass