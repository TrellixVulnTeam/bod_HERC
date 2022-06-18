import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV, list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.input import output_classifier
url = "https://github.com/sociocom/covid19_dataset"
try:
    dir_fs = os.path.dirname(os.path.realpath(__file__))
    git_download(dir_fs, 'covid19_dataset',url)
except:
    pass


def get_data():
    covid19_dataset_en = get_path(dir_fs, 'covid19_dataset',"microblog_ids/en")
    covid19_dataset_ja = get_path(dir_fs, 'covid19_dataset',"microblog_ids/ja")
    covid19_dataset_zh = get_path(dir_fs, 'covid19_dataset',"microblog_ids/zh")
    files = list_file(covid19_dataset_en) 
    path = random.choice(files)
    a = TSV (path, delimiter="\t")
    a_list = []
    for i in a:
        for topic in i["keywords"].split(","):
           a_list.append(output_classifier(topic,"topic"))
        print(a_list)
        print(i.keys())
        print(i["id"])
        print(i["keywords"].split(","))
    
