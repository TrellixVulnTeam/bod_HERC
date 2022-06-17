url = "https://nlp.stanford.edu/~zijwang/talkdown/talkdown.tar.gz"
import os
from machine_learning.exter_dataset.uitls.download import gz_tar_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(dir_fs,"talkdown",url,name=None)


def get_data():
    path = get_path(dir_fs, 'talkdown',"ToLD-BR.csv")