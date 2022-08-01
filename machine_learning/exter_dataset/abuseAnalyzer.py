import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.lalble_key import Hate, HateTargetLabels, HateTargetType


from transformers import BertTokenizer
url = "https://github.com/mohit3011/AbuseAnalyzer"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'abuseAnalyzer',url)


def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    top_tweets = get_path(dir_fs, 'abuseAnalyzer',"AbuseAnalyzer_Dataset.tsv")
    data = TSV(top_tweets)
    data = random.choice(data)
    if data["Hate/Non-Hate"] == "1":
        # Hate
        Hate.Hate
    else:
        Hate.NoHate
    
    if data["Target of Hate"] == "1-2":
        HateTargetLabels.IndividualSecondPerson
        # Individual Second Person
        pass
    elif data["Target of Hate"] == "1-3":
        HateTargetLabels.IndividualThirdPerson
        # Individual Third Person
        pass
    elif data["Target of Hate"] == "2":
        HateTargetLabels.Group
        # Group
        pass
    else:
        pass
    
    if data["Class of Hate"] == "1":
        HateTargetType.BiasedAttitude
        # Biased Attitude
        pass
    elif data["Class of Hate"] == "2":
        HateTargetType.ActOfBiasAndDiscrimination
        # Act of Bias and Discrimination
        pass
    elif data["Class of Hate"] == "3":
        HateTargetType.ViolenceAndGenocide
        # Violence and Genocide
        pass
    else:
        pass
    data["Target of Hate"]
    # tokens, mask, c = tokenizer(data["Post Text"], "Text", "unknown", None)