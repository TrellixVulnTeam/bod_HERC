
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import file_download, zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path

dir_fs = os.path.dirname(os.path.realpath(__file__))
url = "http://people.csail.mit.edu/bce/mistaken/data/scenes.json"
file_download(dir_fs, 'mistaken',url)
url = "http://people.csail.mit.edu/bce/mistaken/data/annotations.json"
file_download(dir_fs, 'mistaken',url)
url = "http://people.csail.mit.edu/bce/mistaken/data/images.zip"
zip_download(dir_fs, 'mistaken',url)





def get_data():
    pass