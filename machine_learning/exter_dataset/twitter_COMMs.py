import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.input import input_twitter_post, output_classifier, output_float
from machine_learning.exter_dataset.uitls.modle import midline
try:
    url = "https://github.com/GiscardBiamby/Twitter-COMMs"
    dir_fs = os.path.dirname(os.path.realpath(__file__))
    git_download(dir_fs, 'Twitter-COMMs',url)
except:
    pass

def get_data():
    path ="data/tweets/twitter_comms_dataset.csv"
    path = get_path(dir_fs, 'Twitter-COMMs',path)
    a = random.choice(CSV(path))
    tw = input_twitter_post(a["tweet_id"],"eng")
    classifier = output_classifier(a["topic"],"topic")
    possibly_sensitive = output_classifier(a["possibly_sensitive"],"possibly_sensitive")
    nsfw_prob = output_float(a['nsfw_prob'],'nsfw_prob')
    return midline(in_=[tw],middle=[classifier,possibly_sensitive,nsfw_prob])
