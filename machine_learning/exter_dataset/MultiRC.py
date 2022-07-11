import os

from machine_learning.exter_dataset.uitls.download import zip_download


url = "https://cogcomp.seas.upenn.edu/multirc/data/mutlirc-v2.zip"

base_path = os.path.dirname(os.path.realpath(__file__))
zip_download(base_path,"mutlirc",url,name=None)





def get_data():
    pass