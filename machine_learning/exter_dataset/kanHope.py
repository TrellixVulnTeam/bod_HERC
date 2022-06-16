import os
from machine_learning.exter_dataset.uitls.download import zenodo_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
url = "https://zenodo.org/record/4904729#.YoVh_3XMKV4"
zenodo_download(dir_fs,"Hope Speech detection in Under-resourced Kannada language","904729")



def get_data():
    pass