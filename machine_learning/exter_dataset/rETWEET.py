import os
from machine_learning.exter_dataset.uitls.download import kaggle_download


url = "https://www.kaggle.com/datasets/soroosharasteh/retweet"

dir_fs = os.path.dirname(os.path.realpath(__file__))
kaggle_download(dir_fs,"soroosharasteh","retweet","test_gold.txt")
kaggle_download(dir_fs,"soroosharasteh","retweet","train_final_label.txt")
kaggle_download(dir_fs,"soroosharasteh","retweet","train_reply_labels_set1.txt")
kaggle_download(dir_fs,"soroosharasteh","retweet","train_reply_labels_set2.txt")


def get_data():
    pass
