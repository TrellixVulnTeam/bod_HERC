import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV  
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/JerryWei03/NewB"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'NewB',url)



def get_data():
    path_conservative = get_path(dir_fs, 'NewB',"conservative.txt")
    path_liberal = get_path(dir_fs, 'NewB',"liberal.txt")
    path = random.choice([ path_conservative, path_liberal])
    data = random.choice(CSV(path))
    if "liberal.txt" in path:
        pass
    elif "conservative.txt" in path:
        pass
    data[1]