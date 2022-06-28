import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import file_download, git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/dD2405/Twitter_Sentiment_Analysis"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Twitter_Sentiment_Analysis',url)
file_download(dir_fs,'Twitter_Sentiment_Analysis','https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/test.csv',name= "main_test.csv")
file_download(dir_fs,'Twitter_Sentiment_Analysis','https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv',name="main_train.csv")


def get_data():
    if random.choice([False,True]):
        main_train_path = get_path(dir_fs, 'Twitter_Sentiment_Analysis',"main_train.csv")
        data = CSV(main_train_path)
        if data["label"] == "1":
            pass
        elif data["label"] == "0":
            pass
        data["tweet"]
    else:
        main_train_path = get_path(dir_fs, 'Twitter_Sentiment_Analysis',"train.csv")
        data = CSV(main_train_path)
        if data["label"] == "1":
            pass
        elif data["label"] == "0":
            pass
        data["id"]