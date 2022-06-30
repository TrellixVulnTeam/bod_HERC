import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://download.microsoft.com/download/5/F/3/5F3BC941-E2AD-457F-9372-2EE78515672C/Visual_Question_Generation_dataset_1.0.zip"

dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'Visual_Question_Generation',url)