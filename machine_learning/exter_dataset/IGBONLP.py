
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV, de_zip
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/IgnatiusEzeani/IGBONLP"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'IGBONLP',url)
de_zip(dir_fs,'IGBONLP',"json.zip",where= "json")
de_zip(dir_fs,'IGBONLP',"text.zip",where= "text")





def get_data():
    pass