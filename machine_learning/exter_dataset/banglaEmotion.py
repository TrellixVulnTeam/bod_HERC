import os
from machine_learning.exter_dataset.uitls.download import git_download, zip_download

url = "https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/24xd7w7dhp-1.zip"
dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'banglaEmotion',url)

def get_data():
    pass