import csv
import os
import random
from sysconfig import get_path
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
url = "https://github.com/cuilimeng/CoAID"
git_download(dir_fs, 'CoAID',url)


from transformers import BertTokenizer

def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    date = random.choice(["05-01-2020","07-01-2020","09-01-2020","11-01-2020"])
    file = random.choice(["ClaimFakeCOVID-19.csv","NewsFakeCOVID-19.csv","ClaimFakeCOVID-19_tweets.csv","NewsFakeCOVID-19_tweets.csv","ClaimFakeCOVID-19_tweets_replies.csv","NewsFakeCOVID-19_tweets_replies.csv","ClaimRealCOVID-19.csv","NewsRealCOVID-19.csv","ClaimRealCOVID-19_tweets.csv","NewsRealCOVID-19_tweets.csv","ClaimRealCOVID-19_tweets_replies.csv","NewsRealCOVID-19_tweets_replies.csv"])
    path = get_path(dir_fs, 'CoAID',os.path.join(date,file)),
    path = random.choice(CSV(path))
    if file == "ClaimFakeCOVID-19.csv":
        pass
    elif file == "NewsFakeCOVID-19.csv":
        pass
    elif file == "ClaimFakeCOVID-19_tweets.csv":
        pass
    elif file == "NewsFakeCOVID-19_tweets.csv":
        pass
    elif file == "ClaimFakeCOVID-19_tweets_replies.csv":
        pass
    elif file == "NewsFakeCOVID-19_tweets_replies.csv":
        pass
    elif file == "ClaimRealCOVID-19.csv":
        pass
    elif file == "NewsRealCOVID-19.csv":
        pass
    elif file == "ClaimRealCOVID-19_tweets.csv":
        pass
    elif file == "NewsRealCOVID-19_tweets.csv":
        pass
    elif file == "ClaimRealCOVID-19_tweets_replies.csv":
        pass
    elif file == "NewsRealCOVID-19_tweets_replies.csv":
        pass
    pass