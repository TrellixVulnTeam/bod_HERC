
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
import os
url = "https://github.com/moinnadeem/stereoset.git"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'stereoSet',url)


def get_data():
    # mask == BLANK
    path = get_path(dir_fs, 'stereoSet',"data/dev.json")
    data = load_json(path)
    data = random.choice(data["data"]["intersentence"])
    if  data["target"] == "commander":
        pass
    if  data["target"] == "nurse":
        pass
    if  data["target"] == "butcher":
        pass
    if  data["target"] == "Italy":
        pass
    if  data["target"] == "Iranian":
        pass
    if  data["target"] == "Columbian":
        pass
    if  data["target"] == "Bible":
        pass
    if  data["target"] == "Yemen":
        pass
    if  data["target"] == "delivery man":
        pass
    if  data["target"] == "Ecuador":
        pass
    if  data["target"] == "researcher":
        pass
    if  data["target"] == "historian":
        pass
    if  data["target"] == "gentlemen":
        pass
    if  data["target"] == "Columbian":
        pass
    if  data["target"] == "Muslim":
        pass
    if  data["target"] == "Eriteria":
        pass
    if  data["target"] == "plumber":
        pass
    if  data["target"] == "Britain":
        pass
    if  data["target"] == "guitarist":
        pass
    if  data["target"] == "Ukrainian":
        pass
    if  data["target"] == "Vietnam":
        pass
    if  data["target"] == "Arab":
        pass
    if  data["target"] == "prisoner":
        pass
    if  data["target"] == "Brahmin":
        pass
    if  data["target"] == "Spain":
        pass
    if  data["target"] == "Persian people":
        pass
    if  data["target"] == "performing artist":
        pass
    if  data["target"] == "researcher":
        pass
    if  data["target"] == "Syria":
        pass
    if  data["target"] == "policeman":
        pass
    if  data["target"] == "Somalia":
        pass
    if  data["target"] == "bartender":
        pass
    if  data["target"] == "schoolboy":
        pass
    if  data["target"] == "manager":
        pass
    if  data["target"] == "politician":
        pass
    if  data["target"] == "mathematician":
        pass
    if  data["target"] == "nurse":
        pass
    if  data["target"] == "gentlemen":
        pass
    if  data["target"] == "Bangladesh":
        pass
    if  data["target"] == "grandfather":
        pass
    if  data["target"] == "African":
        pass
    if  data["target"] == "Iraq":
        pass
    if  data["target"] == "policeman":
        pass





    if data["bias_type"] == "race":
        pass
    if data["bias_type"] == "profession":
        pass
    if data["bias_type"] == "gender":
        pass
    data["context"]
    for sentence in data["sentences"]:
        pass