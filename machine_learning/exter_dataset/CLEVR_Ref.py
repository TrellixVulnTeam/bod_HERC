url = "https://cs.jhu.edu/~cxliu/data/clevr_ref+_1.0.zip"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path

dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'clevr_ref',url)

def get_data():
    pass