import os
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/mayelsherif/hate_speech_icwsm18"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate_speech_icwsm18',url)


def get_data():
    politifact_article_mapped = get_path(dir_fs, 'retweet',"formatted_data/Politifact/article_mapped.json")
    politifact_article_mapped = load_json(politifact_article_mapped)
    print(politifact_article_mapped)