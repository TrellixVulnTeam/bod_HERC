url_train = "https://s3.amazonaws.com/my89public/quac/train_v0.2.json"
url_val = "https://s3.amazonaws.com/my89public/quac/val_v0.2.json"

import os
from machine_learning.exter_dataset.uitls.download import file_download

base_path = os.path.dirname(os.path.realpath(__file__))
file_download(base_path,"quac",url_val,name="train_v0.2.json")
file_download(base_path,"quac",url_val,name="val_v0.2.json")

def get_data():
    pass