import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.lalble_key import Hate
url = "https://github.com/t-davidson/hate-speech-and-offensive-language"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate_Speech_and_Offensive_Language',url)


def get_data():
    test_dataset_path = get_path(dir_fs, 'hate_Speech_and_Offensive_Language',"labeled_data.csv")
    data = random.choice(CSV(test_dataset_path))
    if data["hate_speech"] == "1":
        Hate.Hate
    else:
        Hate.NoHate
    if data["offensive_language"] == "1":
        pass
    else:
        pass
    if data["neither"] == "1":
        pass
    else:
        pass
    data["tweet"]
