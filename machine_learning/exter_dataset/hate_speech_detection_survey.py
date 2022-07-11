url =  "https://github.com/richouzo/hate-speech-detection-survey"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.lalble_key import Hate


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hate-speech-detection-survey',url)



def get_data():
    offenseval_val = get_path(dir_fs, 'hate_speech_detection',"offenseval_val.csv")
    data = random.choice(CSV(offenseval_val))
    if data["Label"]== "1":
        Hate.Hate
    elif data["Label"]== "0":
        Hate.NoHate
    data["Youtube_ID"]
    # tokens, mask, c = tokenizer(test_dataset_csv["Speech"] , "Text", "unknown", None)
