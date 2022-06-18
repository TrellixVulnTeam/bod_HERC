import os
from machine_learning.exter_dataset.uitls.download import zenodo_download
from machine_learning.exter_dataset.uitls.get_path import get_path


base_path = os.path.dirname(os.path.realpath(__file__))
zenodo_download(base_path,"PANACEA","6493847")


def get_data():
    pass