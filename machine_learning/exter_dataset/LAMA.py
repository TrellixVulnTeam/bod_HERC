import os
from machine_learning.exter_dataset.uitls.download import zip_download
url = "https://dl.fbaipublicfiles.com/LAMA/data.zip"
dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'LAMA',url)



def get_data():
    pass