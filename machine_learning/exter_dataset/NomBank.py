import os

from machine_learning.exter_dataset.uitls.download import gz_tar_download

url = "https://nlp.cs.nyu.edu/meyers/nombank/nombank.1.0.tgz"

base_path = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(base_path,"nombank",url)



def get_data():
    pass