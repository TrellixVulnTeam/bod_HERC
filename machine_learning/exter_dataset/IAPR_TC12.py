import os
from machine_learning.exter_dataset.uitls.download import gz_tar_download


url = "http://www-i6.informatik.rwth-aachen.de/imageclef/resources/iaprtc12.tgz"

dir_fs = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(dir_fs, 'iaprtc12',url)





def get_data():
    pass