url = "https://scifact.s3-us-west-2.amazonaws.com/release/latest/data.tar.gz"

from machine_learning.exter_dataset.uitls.download import file_download, gz_tar_download, zip_download
import os
dir_fs = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(dir_fs,"SciFact",url)


def get_data():
    pass