import os
from machine_learning.exter_dataset.uitls.download import gz_tar_download


url ="https://dl.fbaipublicfiles.com/flores101/dataset/flores101_dataset.tar.gz"


base_path = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(base_path,"flores101",url)



def get_data():
    pass