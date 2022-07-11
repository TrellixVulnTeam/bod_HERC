from git import Repo
import os

from machine_learning.exter_dataset.uitls.download import file_download
url = "http://dl.fbaipublicfiles.com/KILT/kilt_knowledgesource.json"


dir_fs = os.path.dirname(os.path.realpath(__file__))
file_download(dir_fs, 'KILT',url,name="kilt_knowledgesource.json")

def get_data():
    pass