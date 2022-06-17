import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/JerryWei03/NewB"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'NewB',url)



def get_data():
    path_conservative = get_path(dir_fs, 'NewB',"conservative.txt")
    path_liberal = get_path(dir_fs, 'NewB',"liberal.txt")
    path_test = get_path(dir_fs, 'NewB',"test.txt")
    path_train_orig = get_path(dir_fs, 'NewB',"train_orig.txt")