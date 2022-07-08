import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/germeval2021toxic/SharedTask/"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'SharedTask',url)


def get_data():
    GermEval21_TestData = get_path(dir_fs, 'SharedTask',"Data Sets/GermEval21_TestData.csv")
    GermEval21_TrainData = get_path(dir_fs, 'SharedTask',"Data Sets/GermEval21_TrainData.csv")
    paths = [GermEval21_TestData,GermEval21_TrainData]
    data = random.choice(CSV(random.choice(paths)))
    if data["Sub3_FactClaiming"] == "1":
        pass
    else:
        pass
    if data["Sub2_Engaging"] == "1":
        pass
    else:
        pass
    if data["Sub1_Toxic"] == "1":
        pass
    else:
        pass
    
    # tokens, mask, c = tokenizer(data["comment_text"], "Text", "unknown", None)
    data["comment_text"]

