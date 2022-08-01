import os
import random
import re
from machine_learning.exter_dataset.uitls.decode_data import TSV, list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.lalble_key import BinaryFacts
from transformers import BertTokenizer
url = "https://gitlab.com/bigirqu/ArCOV-19"

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ArCOV-19',url)


def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    all_tweets = get_path(dir_fs, 'ArCOV-19',"dataset/all_tweets")
    top_tweets = get_path(dir_fs, 'ArCOV-19',"dataset/top_tweets")
    path = list_file(random.choice([all_tweets,top_tweets]))
    claim_verification_relevant_tweets = get_path(dir_fs, 'ArCOV-19',"claim_verification/relevant_tweets")
    claim_verification_claims = get_path(dir_fs, 'ArCOV-19',"claim_verification/claims")
    tweet_verification = get_path(dir_fs, 'ArCOV-19',"ArCOV19-Rumors/tweet_verification")
    path_claim_verification_relevant = random.choice(list_file(claim_verification_relevant_tweets))
    path_tweet_verification = random.choice(list_file(tweet_verification))
    
    if random.choice([True,False]):
        data = random.choice(TSV(path_tweet_verification))
        
        if data["label"]== "False":
            boolen_factCheck = False
        elif data["label"]== "True":
            boolen_factCheck = True
            pass
        elif data["label"]== "Other":
            return None
        data["tweetID"]
        return {
            "input":data["tweetText"],
            "boolen_factCheck":boolen_factCheck
        }

    else:
        data = random.choice(TSV(path_tweet_verification))
        if data["ClaimLabel"]== "False":
            boolen_factCheck = False
        elif data["ClaimLabel"]== "True":
            boolen_factCheck = True
        
        if data["Category"]== "Entertainment":
            # Entertainment
            pass
        elif data["Category"]== "Social":
            # Social
            pass
        elif data["Category"]== "Health":
            # Health
            pass
        elif data["Category"]== "Politics":
            # Politics
            pass
        elif data["Category"]== "Sports":
            # Sports
            pass
        elif data["Category"]== "Religious":
            # Religious
            pass
        
        return {
            "input":data["tweetText"],
            "boolen_factCheck":boolen_factCheck
        }
    
    
    
    