url_train ="https://dl.fbaipublicfiles.com/textvqa/data/TextVQA_0.5.1_train.json"
url_train_val_images ="https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

dir_fs = os.path.dirname(os.path.realpath(__file__))
# git_download(dir_fs, 'textvqa',url_train_val_images)





def get_data():
    pass