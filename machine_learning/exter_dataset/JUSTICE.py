import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/smitp415/CSCI_544_Final_Project"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'CSCI_544_Final_Project',url)



def get_data():
    clean_data = get_path(dir_fs, 'CSCI_544_Final_Project',"clean_data.csv")
    SCDB_2021_01_caseCentered_Vote = get_path(dir_fs, 'CSCI_544_Final_Project',"SCDB_2021_01_caseCentered_Vote.csv")
    
