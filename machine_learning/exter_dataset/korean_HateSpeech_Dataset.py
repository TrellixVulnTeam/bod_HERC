import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.lalble_key import Hate, HateGroup, HateOrOffensive
url = "https://github.com/kocohub/korean-hate-speech"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'korean_HateSpeech_Dataset',url)



def get_data():
    test_dataset = get_path(dir_fs, 'korean_HateSpeech_Dataset',"labeled/test.tsv")
    dev_dataset  = get_path(dir_fs, 'korean_HateSpeech_Dataset',"labeled/dev.tsv")
    path = random.choice([test_dataset,dev_dataset])
    data = random.choice(TSV(path))
    if data["hate"] =="none":
        HateOrOffensive.NULL
    elif data["hate"] =="offensive":
        HateOrOffensive.Offensive
        pass
    elif data["hate"] =="hate":
        HateOrOffensive.Hate
    
    if data["bias"] =="none":
        HateGroup.none
    elif data["bias"] =="others":
        HateGroup.Other
    elif data["bias"] =="gender":
        HateGroup.Gender
