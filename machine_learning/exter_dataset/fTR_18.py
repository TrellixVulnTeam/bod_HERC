import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/dcaled/FTR-18"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'FTR-18',url)



def get_data():
    COVIDFACT_dataset = get_path(dir_fs, 'FTR-18',"news_metadata/2018_09_26_news_metadata.csv")
    data = random.choice(CSV(COVIDFACT_dataset,delimiter=";"))
    data["Rumour_id"]
    data["News_id"]
    data["Lang"]
    data["Url"]
    pass