import os
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/t-davidson/hate-speech-and-offensive-language"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate_Speech_and_Offensive_Language',url)


def get_data():
    test_dataset_path = get_path(dir_fs, 'hate_Speech_and_Offensive_Language',"labeled_data.csv")
    data = random.choice(CSV(test_dataset_path))