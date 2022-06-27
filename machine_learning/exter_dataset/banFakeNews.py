import os
from kaggle.api.kaggle_api_extended import KaggleApi

from machine_learning.exter_dataset.uitls.get_path import get_path
name = "cryptexcode/banfakenews"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs,"repo", 'banFakeNews')
try:
    os.mkdir(dir_fs)
except:
    pass
api = KaggleApi()
api.authenticate()
api.dataset_download_files(name,path=dir_fs, unzip=True)
import random

def get_data():
    LabeledFake = get_path(dir_fs, 'banFakeNews',"LabeledFake-1K.csv")
    LabeledAuthentic = get_path(dir_fs, 'banFakeNews',"LabeledAuthentic-7K.csv")
    Fake = get_path(dir_fs, 'banFakeNews',"Fake-1K.csv")
    Authentic = get_path(dir_fs, 'banFakeNews',"Authentic-48K.csv")
    path = random.choice([LabeledFake, LabeledAuthentic,Fake, Authentic])