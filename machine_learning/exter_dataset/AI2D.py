import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download, zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://s3-us-west-2.amazonaws.com/dqa-data/shining3.zip"
dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'dqa-net',url,"data_dqa")

def get_data():
    pass