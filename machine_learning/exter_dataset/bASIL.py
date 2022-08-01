import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


from transformers import BertTokenizer
url = "https://github.com/marshallwhiteorg/emnlp19-media-bias"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'emnlp19-media-bias',url)


def get_data():
    pass