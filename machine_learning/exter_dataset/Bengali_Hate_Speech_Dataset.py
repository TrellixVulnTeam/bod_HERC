url = "https://github.com/rezacsedu/Bengali-Hate-Speech-Dataset"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Bengali-Hate-Speech-Dataset',url)



def get_data():
    bengali_hate = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/")
    path = random.choice(list_file(bengali_hate))
    data = random.choice(CSV(path))
    #
    if bool(data["canceled"]):
        pass
    else:
        pass
    if "alisoneroman" in path:
        pass
    if "armiehammer" in path:
        pass
    if "bobbaffert" in path:
        pass
    if "carson king" in path:
        pass
    if "dojacat " in path:
        pass
    if "gabcake" in path:
        pass
    if "ginacarano" in path:
        pass
    if "goya" in path:
        pass
    if "jamescharles" in path:
        pass
    if "jimmyfallon " in path:
        pass
    if "jk_rowling " in path:
        pass
    if "lana" in path:
        pass
    if "Lin_Manuel" in path:
        pass
    if "morgan wallen" in path:
        pass
    if "pepe le pew" in path:
        pass
    if "pepsi" in path:
        pass
    if "projared" in path:
        pass
    if "sebastian stan" in path:
        pass
    if "seuss" in path:
        pass
    if "shane gillis" in path:
        pass
    if "starbucks" in path:
        pass
    if "UnburntWitch" in path:
        pass
    # tweet
    data["id"]