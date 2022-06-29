import random
from git import Repo
import os
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset"

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Ethos',url)


def get_data():
    # ;
    path_join_testset_levelbhate_speech_and_offensive_language  = get_path(dir_fs, 'Ethos',"ethos/hs_data/hate-speech-and-offensive-language.csv")
    path_join_testset_levelbEthos_Dataset_Multi_Label  = get_path(dir_fs, 'Ethos',"ethos/ethos_data/Ethos_Dataset_Multi_Label.csv")
    path_join_testset_levelbEthos_Dataset_Binary  = get_path(dir_fs, 'Ethos',"ethos/ethos_data/Ethos_Dataset_Binary.csv")
    path = random.choice([path_join_testset_levelbhate_speech_and_offensive_language,path_join_testset_levelbEthos_Dataset_Multi_Label,path_join_testset_levelbEthos_Dataset_Binary])
    data = random.choice(CSV(path,delimiter=";"))
    if data["isHate"] == "1":
        pass
    else:
        pass
    data["comment"] 