import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/gabll/some-like-it-hoax"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'some_Like_it_Hoax',url)



def get_data():
    path = get_path(dir_fs, 'some_Like_it_Hoax',"dataset/hoaxpagedict.json")
    data = load_json(path)
    key = random.choice(data.keys())
    if data[key] == "true":
        pass
    elif data[key] == "false":
        pass