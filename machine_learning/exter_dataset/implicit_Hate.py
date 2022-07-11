url = "https://www.dropbox.com/s/24meryhqi1oo0xk/implicit-hate-corpus-nov-2021.zip?dl=0"


import os
from machine_learning.exter_dataset.uitls.download import zip_download

base_path = os.path.dirname(os.path.realpath(__file__))
zip_download(base_path,"implicit-hate-corpus-nov-2021",url)


def get_data():
    pass