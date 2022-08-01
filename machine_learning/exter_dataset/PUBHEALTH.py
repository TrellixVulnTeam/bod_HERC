import os
import random
from time import pthread_getcpuclockid
from machine_learning.data_url import load_url
from machine_learning.exter_dataset.uitls.decode_data import CSV, TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.service_scrap.modules.retrieval import Memory_Handler, Retrieval
from machine_learning.service_scrap.modules.retrieval import Memory_Handler


url = "https://github.com/neemakot/Health-Fact-Checking"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Health-Fact-Checking',url)




def get_data():
    dev_dataset = get_path(dir_fs, 'Health-Fact-Checking/PUBHEALTH',"dev.tsv")
    test_dataset = get_path(dir_fs, 'Health-Fact-Checking/PUBHEALTH',"test.tsv")
    train_dataset = get_path(dir_fs, 'Health-Fact-Checking/PUBHEALTH',"train.tsv")
    data = random.choice(TSV(random.choice([train_dataset,test_dataset,dev_dataset])))
    for source in data["sources"].split(","):
            try:
                text = load_url(source)
            except:
                continue