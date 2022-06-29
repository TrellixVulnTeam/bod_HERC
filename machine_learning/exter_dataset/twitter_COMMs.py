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
    tw = a["tweet_id"]
    nsfw_prob = a['nsfw_prob']
    if      a["topic"] == "climate":
        pass
    elif    a["topic"] == "covid":
        pass
    if      a["possibly_sensitive"] == "False":
        pass
    elif    a["possibly_sensitive"] == "True":
        pass
