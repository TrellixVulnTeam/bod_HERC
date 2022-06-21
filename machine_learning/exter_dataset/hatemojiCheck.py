import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, de_zip 
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/HannahKirk/Hatemoji"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Hatemoji',url)
de_zip(dir_fs,'Hatemoji',"data/rotoedit.tar.bz2")
de_zip(dir_fs,'Hatemoji',"data/webedit.tar.bz2")

def get_data():
    HatemojiBuild_test = get_path(dir_fs, 'Hatemoji',"HatemojiBuild/test.csv")
    HatemojiBuild_train = get_path(dir_fs, 'Hatemoji',"HatemojiBuild/train.csv")
    HatemojiBuild_validation = get_path(dir_fs, 'Hatemoji',"HatemojiBuild/validation.csv")
    HatemojiCheck_test = get_path(dir_fs, 'Hatemoji',"HatemojiCheck/test.csv")
    path = random.choices([HatemojiBuild_test,HatemojiBuild_train,HatemojiBuild_validation,HatemojiCheck_test])
    data = random.choices(CSV(path))
    