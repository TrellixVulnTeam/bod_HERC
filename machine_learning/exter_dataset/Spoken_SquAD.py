import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV, load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/chiahsuan156/Spoken-SQuAD"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Spoken-SQuAD',url)





def get_data():
    if random.choice([True,False]):
        path = get_path(dir_fs, 'Spoken-SQuAD',"data/raw.json")
        data = random.choice(load_json(path))
        for chinese in data["chinese"]:
            pass
        for book in data["book"]:
            pass
        for google in data["google"]:
            pass
        for deepl in data["deepl"]:
            pass
    else:
        path = get_path(dir_fs, 'Spoken-SQuAD',"filtered.json")
        data = random.choice(load_json(path))
        for chinese in data["chinese"]:
            pass
        data["gold"]
        for machine in data["machine"]:
            pass
        for human in data["human"]:
            pass