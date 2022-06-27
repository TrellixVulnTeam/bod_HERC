url =  "https://github.com/richouzo/hate-speech-detection-survey"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate-speech-detection-survey',url)



def get_data():
    offenseval_test = get_path(dir_fs, 'hate_speech_detection',"offenseval_test.csv")
    offenseval_train = get_path(dir_fs, 'hate_speech_detection',"offenseval_train.csv")
    offenseval_val = get_path(dir_fs, 'hate_speech_detection',"offenseval_val.csv")
    path = random.choice([offenseval_test,offenseval_train,offenseval_val])
    data = random.choice(CSV(path))