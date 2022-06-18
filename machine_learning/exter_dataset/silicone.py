url = "https://huggingface.co/datasets/silicone#dataset-structure"
import os
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.download import huggingface_download

try:
    dir_fs = os.path.dirname(os.path.realpath(__file__))
    huggingface_download(dir_fs,'silicone','silicone', 'dyda_da')
except:
    pass

def get_data():
    pass