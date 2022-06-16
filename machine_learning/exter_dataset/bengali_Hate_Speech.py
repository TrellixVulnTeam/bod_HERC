import os
from machine_learning.exter_dataset.uitls.download import git_download

url = "https://github.com/rezacsedu/Bengali-Hate-Speech-Dataset"

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'bengali_Hate_Speech',url)

