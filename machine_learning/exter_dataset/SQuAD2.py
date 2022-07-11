url= "https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json"

import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download, gz_tar_download ,file_download
from machine_learning.exter_dataset.uitls.get_path import get_path

dir_fs = os.path.dirname(os.path.realpath(__file__))
file_download(dir_fs, 'SQuAD-explorer',url)