import os
from machine_learning.exter_dataset.uitls.download import git_download

url = "https://github.com/HKUST-KnowComp/MLMA_hate_speech"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'mLMA_Hate_Speech',url)


def get_data():
    pass