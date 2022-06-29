import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
url = "https://github.com/JerryWei03/COVID-Q"
git_download(dir_fs, 'COVID-Q',url)


def get_data():
    final_master_dataset = get_path(dir_fs, 'COVID-Q',"data/final_master_dataset.csv")
    data = CSV(final_master_dataset)
    data= random.choice(data)
    Question = data["Question"]
    Answers = data["Answers"]