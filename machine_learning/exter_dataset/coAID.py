import os
import random
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/cuilimeng/CoAID"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'CoAID',url)


def get_data():
    i = random.randint(0,4)
    if i == 0:
        paths = [
        get_path(dir_fs, 'CoAID',"05-01-2020/ClaimFakeCOVID-19_tweets.csv"),
        get_path(dir_fs, 'CoAID',"05-01-2020/ClaimRealCOVID-19_tweets.csv")
        ]
        path = random.choice(paths)
        if "Fake" in path:
            pass
        if "Real" in path:
            pass
    if i == 1:
        paths = [
        get_path(dir_fs, 'CoAID',"05-01-2020/NewsFakeCOVID-19_tweets.csv"),
        get_path(dir_fs, 'CoAID', "05-01-2020/NewsRealCOVID-19_tweets.csv")
        ]
        path = random.choice(paths)
        if "Fake" in path:
            pass
        if "Real" in path:
            pass
    if i == 2:
        paths = [
        get_path(dir_fs, 'CoAID',"07-01-2020/ClaimFakeCOVID-19_tweets_replies.csv"),
        get_path(dir_fs, 'CoAID',"05-01-2020/ClaimFakeCOVID-19_tweets_replies.csv")
        ]
        path = random.choice(paths)
        if "Fake" in path:
            pass
        if "Real" in path:
            pass
    if i == 3:
        paths = [
        get_path(dir_fs, 'CoAID', "05-01-2020/NewsFakeCOVID-19.csv"),
        get_path(dir_fs, 'CoAID', "05-01-2020/NewsRealCOVID-19.csv"),
        get_path(dir_fs, 'CoAID', "07-01-2020/NewsFakeCOVID-19.csv"),
        get_path(dir_fs, 'CoAID', "07-01-2020/NewsRealCOVID-19.csv"),
        get_path(dir_fs, 'CoAID', "09-01-2020/NewsFakeCOVID-19.csv"),
        get_path(dir_fs, 'CoAID', "09-01-2020/NewsRealCOVID-19.csv"),
        get_path(dir_fs, 'CoAID', "11-01-2020/NewsFakeCOVID-19.csv"),
        get_path(dir_fs, 'CoAID', "11-01-2020/NewsRealCOVID-19.csv")
        ]
        path = random.choice(paths)
        if "Fake" in path:
            pass
        if "Real" in path:
            pass
    
    if i == 4:
        paths = [
        get_path(dir_fs, 'CoAID',"07-01-2020/ClaimFakeCOVID-19.csv"),
        get_path(dir_fs, 'CoAID',"07-01-2020/ClaimRealCOVID-19.csv"),
        get_path(dir_fs, 'CoAID',"09-01-2020/ClaimFakeCOVID-19.csv"),
        get_path(dir_fs, 'CoAID',"09-01-2020/ClaimRealCOVID-19.csv"),
        get_path(dir_fs, 'CoAID',"11-01-2020/ClaimFakeCOVID-19.csv"),
        get_path(dir_fs, 'CoAID',"11-01-2020/ClaimRealCOVID-19.csv")
        ]
        path = random.choice(paths)
        if "Fake" in path:
            pass
        if "Real" in path:
            pass
    # fact_check_url,archive,news_url,news_url2,news_url3,news_url4,news_url5