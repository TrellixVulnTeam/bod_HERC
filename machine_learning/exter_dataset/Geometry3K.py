url_train = "https://lupantech.github.io/inter-gps/geometry3k/train.zip"
url_logic_forms = "https://lupantech.github.io/inter-gps/geometry3k/logic_forms.zip"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path

dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'geometry3k',url_logic_forms)
zip_download(dir_fs, 'geometry3k',url_train)

def get_data():
    pass