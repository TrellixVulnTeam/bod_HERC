url =  "https://github.com/richouzo/hate-speech-detection-survey"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate-speech-detection-survey',url)



def get_data():
    pass