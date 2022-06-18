import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/mly-nlp/LJP-MSJudge"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'LJP-MSJudge',url)
path = get_path(dir_fs, 'LJP-MSJudge',"microblog_ids/en")

def get_data():
    path = get_path(dir_fs, 'LJP-MSJudge',"microblog_ids/en")
