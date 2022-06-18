url = "https://github.com/Justus-Jonas/Cancel-Culture-Corpus"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Cancel-Culture-Corpus',url)



def get_data():
    pass