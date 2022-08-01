import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.input import input_twitter_post, output_classifier, output_float
from machine_learning.exter_dataset.uitls.modle import midline
from machine_learning.service.twitter import tweet_downloader
from transformers import BertTokenizer
try:
    url = "https://github.com/GiscardBiamby/Twitter-COMMs"
    dir_fs = os.path.dirname(os.path.realpath(__file__))
    git_download(dir_fs, 'Twitter-COMMs',url)
except:
    pass

def get_data():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    path ="data/tweets/twitter_comms_dataset.csv"
    path = get_path(dir_fs, 'Twitter-COMMs',path)
    a = random.choice(CSV(path))
    text = tweet_downloader(a["tweet_id"])
    inputs = tokenizer(text, return_tensors="pt")
    nsfw_prob = a['nsfw_prob']
    if      a["topic"] == "climate":
        pass
    elif    a["topic"] == "covid":
        pass
    if      a["possibly_sensitive"] == "False":
        pass
    elif    a["possibly_sensitive"] == "True":
        pass
