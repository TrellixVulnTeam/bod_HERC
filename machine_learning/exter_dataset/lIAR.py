from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import  zip_download
import os
import random
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://www.cs.ucsb.edu/~william/data/liar_dataset.zip"
dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs,"liar_dataset",url)



def get_data():
    test_dataset = get_path(dir_fs, 'liar_dataset',"test.tsv")
    train_dataset = get_path(dir_fs, 'liar_dataset',"train.tsv")
    valid_dataset = get_path(dir_fs, 'liar_dataset',"valid.tsv")
    path = random.choice([test_dataset,train_dataset,valid_dataset])
    data = TSV(path)