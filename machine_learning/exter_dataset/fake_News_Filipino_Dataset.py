import os

from machine_learning.exter_dataset.uitls.download import zip_download

url = "https://s3.us-east-2.amazonaws.com/blaisecruz.com/datasets/fakenews/fakenews.zip"
base_path = os.path.dirname(os.path.realpath(__file__))
zip_download(base_path,"flores101",url)



def get_data():
    pass