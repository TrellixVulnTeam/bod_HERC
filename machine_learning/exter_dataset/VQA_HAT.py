import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path

vqahat_train_url = "https://computing.ece.vt.edu/~abhshkdz/data/vqahat/vqahat_train.zip"
vqahat_val_url = "https://computing.ece.vt.edu/~abhshkdz/data/vqahat/vqahat_val.zip"

dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'vqahat',vqahat_train_url,name="vqahat_train")
zip_download(dir_fs, 'vqahat',vqahat_val_url,name="vqahat_val")

zip_download(dir_fs, 'vqahat',"https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Train_mscoco.zip",name="v2_Annotations_Train_mscoco")
zip_download(dir_fs, 'vqahat',"https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Val_mscoco.zip",name="v2_Annotations_Val_mscoco")



def get_data():
    pass