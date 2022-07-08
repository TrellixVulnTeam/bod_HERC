import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV, list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.lalble_key import BinaryFacts
url = "https://gitlab.com/bigirqu/ArCOV-19"

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ArCOV-19',url)


def get_data():
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
            BinaryFacts.NO
            pass
        elif data["label"]== "True":
            BinaryFacts.YES
            pass
        elif data["label"]== "Other":
            pass
        data["tweetText"]
        # tokens, mask, c = tokenizer(data["tweetText"] , "Text", "unknown", None)
        data["tweetID"]
    else:
        data = random.choice(TSV(path_tweet_verification))
        if data["ClaimLabel"]== "False":
            BinaryFacts.NO
        elif data["ClaimLabel"]== "True":
            BinaryFacts.YES
        
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
        # tokens, mask, c = tokenizer(data["Claim"] , "Text", "unknown", None)
        
    
    
    
    