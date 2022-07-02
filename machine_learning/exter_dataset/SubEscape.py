import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import gz_tar_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url_SubEdits = "https://github.com/shamilcm/pedra/releases/download/v1.0/subedits-en-de-v1-0.tar.gz"
url_SubEscape = "https://github.com/shamilcm/pedra/releases/download/v1.0/subescape-en-de-v1-0.tar.gz"
dir_fs = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(dir_fs,"pedra",url_SubEdits,name="SubEdits")
gz_tar_download(dir_fs,"pedra",url_SubEscape,name="SubEscape")





def get_data():
    pass