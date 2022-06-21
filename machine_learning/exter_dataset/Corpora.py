url = "https://github.com/GloriaComandini/Corpora"
import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Corpora',url)



def get_data():
    corpora = get_path(dir_fs, 'Corpora',"POP-HS-IT.xlsx")