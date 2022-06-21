import os
from machine_learning.exter_dataset.uitls.download import file_download, git_download
url = "https://github.com/dD2405/Twitter_Sentiment_Analysis"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Twitter_Sentiment_Analysis',url)
file_download(dir_fs,'Twitter_Sentiment_Analysis','https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/test.csv',name= "main_test.csv")
file_download(dir_fs,'Twitter_Sentiment_Analysis','https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv',name="main_train.csv")
def get_data():
    pass