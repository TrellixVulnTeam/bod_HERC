import os

from machine_learning.exter_dataset.uitls.download import google_download_file
url = "https://drive.google.com/file/d/1xrD9bL78mbxpp-DdOw1EHhz1nzin_6dX/view"

base_path = os.path.dirname(os.path.realpath(__file__))
google_download_file(base_path,"Samanantar","1xrD9bL78mbxpp-DdOw1EHhz1nzin_6dX","v3")



def get_data():
    pass