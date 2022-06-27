url = "https://github.com/faisalisafk/hate_speech_detection"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate_speech_detection',url)



def get_data():
    hate_speech_detection = get_path(dir_fs, 'hate_speech_detection',"vid.csv")
    data = random.choice(CSV(hate_speech_detection))