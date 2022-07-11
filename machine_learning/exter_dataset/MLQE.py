import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV, de_gz_tar
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url ="https://github.com/facebookresearch/mlqe"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'mlqe',url)



de_gz_tar(dir_fs,"mlqe","data/en-de.tar.gz",output_path="en-de")
de_gz_tar(dir_fs,"mlqe","data/en-de_test.tar.gz",output_path="en-de_test")
de_gz_tar(dir_fs,"mlqe","data/en-zh.tar.gz",output_path="en-zh")
de_gz_tar(dir_fs,"mlqe","data/en-zh_test.tar.gz",output_path="en-zh_test")
de_gz_tar(dir_fs,"mlqe","data/et-en.tar.gz",output_path="et-en")
de_gz_tar(dir_fs,"mlqe","data/et-en_test.tar.gz",output_path="et-en_test")
de_gz_tar(dir_fs,"mlqe","data/ne-en.tar.gz",output_path="ne-en")
de_gz_tar(dir_fs,"mlqe","data/ne-en_test.tar.gz",output_path="ne-en_test")
de_gz_tar(dir_fs,"mlqe","data/ro-en.tar.gz",output_path="ro-en")
de_gz_tar(dir_fs,"mlqe","data/ro-en_test.tar.gz",output_path="ro-en_test")
de_gz_tar(dir_fs,"mlqe","data/si-en.tar.gz",output_path="si-en")
de_gz_tar(dir_fs,"mlqe","data/si-en_test.tar.gz",output_path="si-en_test")
de_gz_tar(dir_fs,"mlqe","data-multi-hyp/data.tar.gz",output_path="data")



def get_data():
    pass