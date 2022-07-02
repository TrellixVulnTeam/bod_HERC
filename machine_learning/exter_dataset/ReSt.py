url = "https://github.com/alessandrocuda/ReSt"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.lalble_key import Hate


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ReSt',url)

def get_data():
    path1 = get_path(dir_fs, 'ReSt',"dataset/haspeede2/preprocessed/dev/dev.json")
    path2 = get_path(dir_fs, 'ReSt',"dataset/haspeede2/preprocessed/reference/reference_news.csv")
    path3 = get_path(dir_fs, 'ReSt',"dataset/haspeede2/preprocessed/reference/reference_news.csv")
    path = random.choice([path1,path2,path3])
    data1 = TSV(path)
    if data1["hs"] == "1":
        Hate.Hate
    else:
        Hate.NoHate
    if data1["stereotype"] == "1":
        pass
    else:
        pass
    data1["text"]