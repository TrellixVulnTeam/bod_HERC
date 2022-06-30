url = "https://www.cl.uni-heidelberg.de/statnlpgroup/wikicaps/wikicaps_v1.0.tar.gz"

import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import gz_tar_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(dir_fs,"wikicaps",url)