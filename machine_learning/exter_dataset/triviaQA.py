url = "http://nlp.cs.washington.edu/triviaqa/data/triviaqa-rc.tar.gz"

import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download, gz_tar_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(dir_fs, 'triviaqa',url)



def get_data():
    pass