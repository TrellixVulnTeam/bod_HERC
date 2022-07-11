url = "https://msmarco.blob.core.windows.net/msmarco/train_v2.1.json.gz"

import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import file_download
from machine_learning.exter_dataset.uitls.get_path import get_path

dir_fs = os.path.dirname(os.path.realpath(__file__))
file_download(dir_fs, 'msmarco',url)





def get_data():
    pass