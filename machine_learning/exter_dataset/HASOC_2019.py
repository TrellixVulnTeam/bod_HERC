url = "https://github.com/TharinduDR/HASOC-2019"
import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'HASOC-2019',url)



def get_data():
    HASOC_2019 = get_path(dir_fs, 'HASOC-2019',"labeled_data.csv")
