url = "https://ai2-public-datasets.s3.amazonaws.com/qasc/qasc_dataset.tar.gz"


import os
from machine_learning.exter_dataset.uitls.download import gz_tar_download, zip_download 

base_path = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(base_path,"qasc",url,name=None)




def get_data():
    pass