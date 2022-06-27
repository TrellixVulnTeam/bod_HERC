url = "https://scifact.s3-us-west-2.amazonaws.com/release/latest/data.tar.gz"
from cmath import e
import random
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import file_download, gz_tar_download, zip_download
import os
from machine_learning.exter_dataset.uitls.get_path import get_path
try:
    dir_fs = os.path.dirname(os.path.realpath(__file__))
    gz_tar_download(dir_fs,"SciFact",url)
except:
    pass

def get_data():
    path = get_path(dir_fs, 'SciFact',"data/claims_dev.jsonl")
    path2 = get_path(dir_fs, 'SciFact',"data/corpus.jsonl")
    data = random.choice(load_jsonl(random.choice([path,path2])))