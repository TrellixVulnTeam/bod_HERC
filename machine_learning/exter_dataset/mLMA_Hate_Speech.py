import os
import random
from machine_learning.exter_dataset.uitls.decode_data import de_zip
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


url = "https://github.com/HKUST-KnowComp/MLMA_hate_speech"
dir_fs = os.path.dirname(os.path.realpath(__file__))
try:
    git_download(dir_fs, 'mLMA_Hate_Speech',url)
except:
    pass
de_zip(dir_fs,'mLMA_Hate_Speech',"hate_speech_mlma.zip")

def get_data():
    ar_dataset_path = get_path(dir_fs, 'mLMA_Hate_Speech',"hate_speech_mlma/ar_dataset.csv")
    en_dataset_path = get_path(dir_fs, 'mLMA_Hate_Speech',"hate_speech_mlma/en_dataset.csv")
    fr_dataset_path = get_path(dir_fs, 'mLMA_Hate_Speech',"hate_speech_mlma/fr_dataset.csv")
    path = random.choice([
        ar_dataset_path,
        en_dataset_path,
        fr_dataset_path
    ])