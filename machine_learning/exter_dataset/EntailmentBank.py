url1 = "https://github.com/allenai/entailment_bank"
url2 = "https://drive.google.com/drive/folders/1YjjeZy9FEbXh-84-HjqOu8Rfve9oj1Te"
import os
from machine_learning.exter_dataset.uitls.download import git_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'EntailmentBank',url1)
# need to add google dive maybe


def get_data():
    pass