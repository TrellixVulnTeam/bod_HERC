train_url = "https://ivc.ischool.utexas.edu/VizWiz_final/images/train.zip"
annotations_url = "http://ivc.ischool.utexas.edu/VizWiz_final/image_quality/annotations.zip"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path

dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs, 'VizWiz_final',train_url,name="VizWiz_final_train.zip")
zip_download(dir_fs, 'VizWiz_final',annotations_url,name="VizWiz_final_annotations.zip")








def get_data():
    pass