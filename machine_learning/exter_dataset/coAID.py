import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/cuilimeng/CoAID"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'CoAID',url)


def get_data():
    ClaimFakeCOVID_tweets_05_01_2020 = get_path(dir_fs, 'CoAID',"05-01-2020/ClaimFakeCOVID-19_tweets.csv")
    ClaimFakeCOVID_05_01_2020 = get_path(dir_fs, 'CoAID',"05-01-2020/ClaimFakeCOVID-19.csv")
    ClaimFakeCOVID_tweets_05_01_2020 = get_path(dir_fs, 'CoAID',"05-01-2020/ClaimRealCOVID-19_tweets.csv")
    ClaimRealCOVID_05_01_2020 = get_path(dir_fs, 'CoAID',"05-01-2020/ClaimRealCOVID-19.csv")
    ClaimRealCOVID_tweets_05_01_2020 = get_path(dir_fs, 'CoAID',"05-01-2020/NewsFakeCOVID-19_tweets.csv")
    NewsFakeCOVID_05_01_2020 = get_path(dir_fs, 'CoAID', "05-01-2020/NewsFakeCOVID-19.csv")
    NewsRealCOVID_05_01_2020 = get_path(dir_fs, 'CoAID', "05-01-2020/NewsRealCOVID-19.csv")
    NewsRealCOVID_tweets_05_01_2020 = get_path(dir_fs, 'CoAID', "05-01-2020/NewsRealCOVID-19_tweets.csv")
    
    
    ClaimFakeCOVID = get_path(dir_fs, 'CoAID',"07-01-2020/ClaimFakeCOVID-19.csv")
    ClaimRealCOVID = get_path(dir_fs, 'CoAID',"07-01-2020/ClaimRealCOVID-19.csv")
    NewsFakeCOVID = get_path(dir_fs, 'CoAID', "07-01-2020/NewsFakeCOVID-19.csv")
    NewsRealCOVID = get_path(dir_fs, 'CoAID', "07-01-2020/NewsRealCOVID-19.csv")
    
    
    ClaimFakeCOVID = get_path(dir_fs, 'CoAID',"09-01-2020/ClaimFakeCOVID-19.csv")
    ClaimRealCOVID = get_path(dir_fs, 'CoAID',"09-01-2020/ClaimRealCOVID-19.csv")
    NewsFakeCOVID = get_path(dir_fs, 'CoAID', "09-01-2020/NewsFakeCOVID-19.csv")
    NewsRealCOVID = get_path(dir_fs, 'CoAID', "09-01-2020/NewsRealCOVID-19.csv")
    
    
    ClaimFakeCOVID = get_path(dir_fs, 'CoAID',"11-01-2020/ClaimFakeCOVID-19.csv")
    ClaimRealCOVID = get_path(dir_fs, 'CoAID',"11-01-2020/ClaimRealCOVID-19.csv")
    NewsFakeCOVID = get_path(dir_fs, 'CoAID', "11-01-2020/NewsFakeCOVID-19.csv")
    NewsRealCOVID = get_path(dir_fs, 'CoAID', "11-01-2020/NewsRealCOVID-19.csv")