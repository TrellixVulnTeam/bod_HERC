import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/mohit3011/AbuseAnalyzer"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'abuseAnalyzer',url)


def get_data():
    top_tweets = get_path(dir_fs, 'abuseAnalyzer',"AbuseAnalyzer_Dataset.tsv")
    data = TSV(top_tweets)
    data = random.choice(data)
    if data["Hate/Non-Hate"] == "1":
        # Hate
        pass
    else:
        # Non-Hate
        pass
    
    if data["Target of Hate"] == "1-2":
        # Individual Second Person
        pass
    elif data["Target of Hate"] == "1-3":
        # Individual Third Person
        pass
    elif data["Target of Hate"] == "2":
        # Group
        pass
    else:
        pass
    
    if data["Class of Hate"] == "1":
        # Biased Attitude
        pass
    elif data["Class of Hate"] == "2":
        # Act of Bias and Discrimination
        pass
    elif data["Class of Hate"] == "3":
        # Violence and Genocide
        pass
    else:
        pass
    data["Target of Hate"]