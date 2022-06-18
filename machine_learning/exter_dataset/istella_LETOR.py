import os
from machine_learning.exter_dataset.uitls.download import gz_tar_download
url = "http://library.istella.it/dataset/istella-letor.tar.gz"
url2 = "http://library.istella.it/dataset/istella-s-letor.tar.gz"
dir_fs = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(dir_fs,"istella",url,name="istella-letor.tar.gz")
gz_tar_download(dir_fs,"istella",url2,name="istella-s-letor.tar.gz")


def get_data():
    pass