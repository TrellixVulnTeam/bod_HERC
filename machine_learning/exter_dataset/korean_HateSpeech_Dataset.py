import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/kocohub/korean-hate-speech"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'korean_HateSpeech_Dataset',url)



def get_data():
    test_dataset = get_path(dir_fs, 'korean_HateSpeech_Dataset',"labeled/test.tsv")
    dev_dataset  = get_path(dir_fs, 'korean_HateSpeech_Dataset',"labeled/dev.tsv")
    path = random.choice([test_dataset,dev_dataset])
    data =TSV(path)
    print(data)