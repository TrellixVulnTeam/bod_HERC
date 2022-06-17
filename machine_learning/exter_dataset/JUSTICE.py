import os
from machine_learning.exter_dataset.uitls.download import git_download

url = "https://github.com/smitp415/CSCI_544_Final_Project"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'CSCI_544_Final_Project',url)



def get_data():
    pass