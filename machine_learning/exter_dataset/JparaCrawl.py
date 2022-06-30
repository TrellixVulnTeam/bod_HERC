url = "http://www.kecl.ntt.co.jp/icl/lirg/jparacrawl/release/3.0/pretrained_models/ja-en/big.tar.gz"


import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import gz_tar_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
gz_tar_download(dir_fs,"jparacrawl",url)