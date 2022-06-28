import os
import random
from sysconfig import get_path
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/JAugusto97/ToLD-Br"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ToLD-Br',url)


def get_data():
    path = get_path(dir_fs, 'ToLD-Br',"ToLD-BR_alpha.csv")
    data = random.choice(CSV(path))
    data["text"]
    if data["homophobia_1"] == "1":
        pass
    else:
        pass
    if data["homophobia_2"] == "1":
        pass
    else:
        pass
    if data["homophobia_3"] == "1":
        pass
    else:
        pass
    if data["obscene_1"] == "1":
        pass
    else:
        pass
    if data["obscene_2"] == "1":
        pass
    else:
        pass
    if data["obscene_3"] == "1":
        pass
    else:
        pass
    if data["insult_1"] == "1":
        pass
    else:
        pass
    if data["insult_2"] == "1":
        pass
    else:
        pass
    if data["insult_3"] == "1":
        pass
    else:
        pass
    if data["racism_1"] == "1":
        pass
    else:
        pass
    if data["racism_2"] == "1":
        pass
    else:
        pass
    if data["racism_3"] == "1":
        pass
    else:
        pass
    if data["misogyny_1"] == "1":
        pass
    else:
        pass
    if data["misogyny_2"] == "1":
        pass
    else:
        pass
    if data["misogyny_3"] == "1":
        pass
    else:
        pass
    if data["xenophobia_1"] == "1":
        pass
    else:
        pass
    if data["xenophobia_2"] == "1":
        pass
    else:
        pass
    if data["xenophobia_3"] == "1":
        pass
    else:
        pass
    if data["obs_1"] == "1":
        pass
    else:
        pass
    if data["obs_2"] == "1":
        pass
    else:
        pass