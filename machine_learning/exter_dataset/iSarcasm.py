import os
import random 
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.service.twitter import tweet_downloader

url = "https://github.com/silviu-oprea/iSarcasm"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'iSarcasm',url)


def get_data():
    dev_dataset = get_path(dir_fs, 'iSarcasm',"isarcasm_test.csv")
    test_dataset = get_path(dir_fs, 'iSarcasm',"isarcasm_train.csv")
    cvs_dev_dataset = CSV(dev_dataset)
    cvs_test_dataset = CSV(test_dataset)
    data = random.choice(cvs_test_dataset+cvs_dev_dataset)
    if data["sarcasm_label"] == "not_sarcastic":
        pass
    elif data["sarcasm_label"] == "sarcastic":
        pass

    if data["sarcasm_type"] == "sarcasm":
        pass
    elif data["sarcasm_type"] == "satire":
        pass
    elif data["sarcasm_type"] == "irony":
        pass
    elif data["sarcasm_type"] == "overstatement":
        pass
    elif data["sarcasm_type"] == "understatement":
        pass
    elif data["sarcasm_type"] == "rhetorical question":
        pass
    text = tweet_downloader(data["tweet_id"])
