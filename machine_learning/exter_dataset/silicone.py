url = "https://huggingface.co/datasets/silicone#dataset-structure"
from datasets import load_dataset
import os
dir_fs = os.path.dirname(os.path.realpath(__file__))
os.mkdir(dir_fs)
dataset = load_dataset('silicone', 'dyda_da',data_dir=dir_fs)




def get_data():
    pass
