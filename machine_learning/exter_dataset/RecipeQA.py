import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import file_download, zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path
train_url = "https://vision.cs.hacettepe.edu.tr/files/recipeqa/train.json"
images_url = "https://vision.cs.hacettepe.edu.tr/files/recipeqa/images.zip"
dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'recipeqa',images_url)
file_download(dir_fs, 'recipeqa',train_url,file="train.json")






def get_data():
    pass