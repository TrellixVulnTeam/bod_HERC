import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "http://tamaraberg.com/visualmadlibs/download/madlibs_train_v2.zip"

dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'madlibs',url)