import os
from machine_learning.exter_dataset.uitls.download import git_download

url = "https://webis.de/data/buzzfeed-webis-fake-news-16.html"
dir_fs = os.path.dirname(os.path.realpath(__file__))
# git_download(dir_fs, 'buzzfeed-webis-fake-news-16',url)



def get_data():
    pass