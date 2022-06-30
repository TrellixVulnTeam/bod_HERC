import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/yanfangh/covid-rumor-stance"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'covid-rumor-stance',url)


def get_data():
    misinformation = get_path(dir_fs, 'covid-rumor-stance',"data/misinformation.csv")
    path = random.choice(misinformation)
    data = random.choice(CSV(path))
    data["news_urls"]
    data["fact_check_urls"]
    data["mis"]
    data["titles"]