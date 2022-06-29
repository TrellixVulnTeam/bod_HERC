url = "https://github.com/c-juhwan/korean-hate-speech-detection"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'korean-hate-speech-detection',url)

def get_data():
    dev_dataset = get_path(dir_fs, 'LAMA',"korean-hate-speech-detection/dataset/dev.hate.csv")
    test_dataset = get_path(dir_fs, 'LAMA',"korean-hate-speech-detection/dataset/train.hate.csv")
    cvs_dev_dataset = random.choice(CSV(random.choice([dev_dataset,test_dataset])))
    