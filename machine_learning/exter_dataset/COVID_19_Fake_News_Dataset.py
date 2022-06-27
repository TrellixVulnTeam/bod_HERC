import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
import os

from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
url = "https://github.com/diptamath/covid_fake_news/"
git_download(dir_fs, 'covid_fake_news',url)


def get_data():
    Constraint_Train = get_path(dir_fs, 'covid_fake_news',"data/Constraint_Train.csv")
    Constraint_Val = get_path(dir_fs, 'covid_fake_news',"data/Constraint_Val.csv")
    english_test_with_labels = get_path(dir_fs, 'covid_fake_news',"data/english_test_with_labels.csv")
    data = random.choice(CSV(random.choice([Constraint_Train,Constraint_Val,english_test_with_labels])))
