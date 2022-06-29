url  = "https://github.com/Gaurav-Pande/hatespeech-detection-dl"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, de_zip
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hatespeech-detection-dl',url)

de_zip(dir_fs,'hatespeech-detection-dl',"chatbots_dataset_final.csv.zip")


def get_data():
    pass