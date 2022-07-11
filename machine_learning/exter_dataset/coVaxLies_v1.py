import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json, load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/Supermaxman/covid19-vaccine-twitter"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'coVaxLies_v1',url)


def get_data():
    coVaxLies_v1_dev = get_path(dir_fs, 'coVaxLies_v1',"annotations/dev.jsonl")
    coVaxLies_v1_test = get_path(dir_fs, 'coVaxLies_v1',"annotations/test.jsonl")
    coVaxLies_v1_train = get_path(dir_fs, 'coVaxLies_v1',"annotations/train.jsonl")
    path = random.choice([coVaxLies_v1_dev,coVaxLies_v1_test,coVaxLies_v1_train])
    data = random.choice(load_jsonl(path))
    misinfo_path = get_path(dir_fs, 'coVaxLies_v1',"annotations/misinfo.json")
    misinfo_data = load_json(misinfo_path)
    load_jsonl(path)
    data["data"]
    for misinfo_key in data["misinfo"].keys():
        data["misinfo"][misinfo_key]
        misinfo_data[misinfo_key]["title"]
        misinfo_data[misinfo_key]["text"]
        misinfo_data[misinfo_key]["alternate_text"]
        misinfo_data[misinfo_key]["source"]
