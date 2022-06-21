import os
import random 
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/silviu-oprea/iSarcasm"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'iSarcasm',url)


def get_data():
    dev_dataset = get_path(dir_fs, 'iSarcasm',"isarcasm_test.csv")
    test_dataset = get_path(dir_fs, 'iSarcasm',"isarcasm_train.csv")
    cvs_dev_dataset = CSV(dev_dataset)
    cvs_test_dataset = CSV(test_dataset)
    data = random.choice(cvs_test_dataset+cvs_dev_dataset)
    print("sarcasm_label:",data["sarcasm_label"])
    print("sarcasm_type:",data["sarcasm_type"])
    print("tweet_id:",data["tweet_id"])