import os
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/mly-nlp/LJP-MSJudge"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'MSJudge',url)
# need to unzip

def get_data():
    pass