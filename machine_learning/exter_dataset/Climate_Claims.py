import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/rahulOmishra/SUMO"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ClimateClaims',url)
    


def get_data():
    climate_fever = get_path(dir_fs, 'climate-fever', "climate_claims_raw.xlsx")