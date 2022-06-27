import os
import random
from machine_learning.exter_dataset.uitls.decode_data import list_file, load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/cyang03/CHECKED"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'CHECKED',url)


def get_data():
    real_news = get_path(dir_fs, 'CHECKED', "dataset/real_news")
    fake_news = get_path(dir_fs, 'CHECKED', "dataset/fake_news")
    data = list_file(random.choice([real_news,fake_news]))
    data = load_json(random.choice(data))