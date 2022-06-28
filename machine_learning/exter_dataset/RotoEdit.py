url = "https://github.com/isomap/factedit"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, de_gz_tar
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'factedit',url)
rotoedit = get_path(dir_fs, 'factedit',"data/rotoedit.tar.bz2")
webedit = get_path(dir_fs, 'factedit',"data/webedit.tar.bz2")
de_gz_tar(dir_fs,'factedit',"data/rotoedit.tar.bz2","rotoedit")
de_gz_tar(dir_fs,'factedit',"data/webedit.tar.bz2","webedit")
def get_data():
    path2 = get_path(dir_fs, 'factedit',"data/RoCStories/100KStories.csv")
    data = random.choice(CSV(path2))