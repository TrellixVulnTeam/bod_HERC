import os
from kaggle.api.kaggle_api_extended import KaggleApi
name = "cryptexcode/banfakenews"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'banFakeNews')
try:
    os.mkdir(dir_fs)
except:
    pass
api = KaggleApi()
api.authenticate()
api.dataset_download_files(name,path=dir_fs, unzip=True)