url  = "https://github.com/Gaurav-Pande/hatespeech-detection-dl"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hatespeech-detection-dl',url)



def get_data():
    pass