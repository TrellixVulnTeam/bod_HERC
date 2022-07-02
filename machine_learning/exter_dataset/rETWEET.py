import os
from machine_learning.exter_dataset.uitls.download import kaggle_download
from machine_learning.exter_dataset.uitls.get_path import get_path

try:
    url = "https://www.kaggle.com/datasets/soroosharasteh/retweet"
    dir_fs = os.path.dirname(os.path.realpath(__file__))
    kaggle_download(dir_fs,"soroosharasteh","retweet","test_gold.txt")
    kaggle_download(dir_fs,"soroosharasteh","retweet","train_final_label.txt")
    kaggle_download(dir_fs,"soroosharasteh","retweet","train_reply_labels_set1.txt")
    kaggle_download(dir_fs,"soroosharasteh","retweet","train_reply_labels_set2.txt")
except:
    pass






def get_data():
    test_gold = get_path(dir_fs, 'retweet',"test_gold.txt")
    train_final_label = get_path(dir_fs, 'retweet',"train_final_label.txt")
    train_reply_labels_set1 = get_path(dir_fs, 'retweet',"train_reply_labels_set1.txt")
    train_reply_labels_set2 = get_path(dir_fs, 'retweet',"train_reply_labels_set2.txt")
