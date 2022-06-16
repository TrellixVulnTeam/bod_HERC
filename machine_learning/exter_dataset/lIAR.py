from machine_learning.exter_dataset.uitls.download import  zip_download
import os
url = "https://www.cs.ucsb.edu/~william/data/liar_dataset.zip"
dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs,"liar_dataset",url)



def get_data():
    pass