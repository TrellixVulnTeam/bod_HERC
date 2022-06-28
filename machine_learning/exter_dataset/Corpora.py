url = "https://github.com/GloriaComandini/Corpora"
import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
import pandas as pd


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Corpora',url)



def get_data():
    corpora = get_path(dir_fs, 'Corpora',"POP-HS-IT.xlsx")
    df = pd.read_excel(corpora, sheet_name='Foglio1')
    datas = df.sample(1)
    for index, data in datas.iterrows():
        if data["hate_speech"] == "yes":
            pass
        else:
            pass
        if data["aggressiveness"] == "yes":
            pass
        else:
            pass
        if data["offensiveness"] == "yes":
            pass
        else:
            pass
        if data["irony"] == "yes":
            pass
        else:
            pass
        if data["stereotype"] == "yes":
            pass
        else:
            pass
        if data["news"] == "yes":
            pass
        else:
            pass
        if data["nominal_utterance"] == "yes":
            pass
        else:
            pass
        text= data["text"]
        id_str= data["id_str"]
