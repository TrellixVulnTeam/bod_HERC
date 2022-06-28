import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/rishabhmisra/News-Headlines-Dataset-For-Sarcasm-Detection"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'News-Headlines-Dataset-For-Sarcasm-Detection',url)



def get_data():
    Sarcasm_Headlines_Dataset = get_path(dir_fs, 'News-Headlines-Dataset-For-Sarcasm-Detection',"Sarcasm_Headlines_Dataset.json")
    data = random.choices(load_jsonl(Sarcasm_Headlines_Dataset))
    data["is_sarcastic"]
    data["headline"]
    data["article_link"]