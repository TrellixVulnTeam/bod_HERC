url = "https://github.com/TharinduDR/HASOC-2019"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'HASOC-2019',url)



def get_data():
    HASOC_2019 = get_path(dir_fs, 'HASOC-2019',"data/labeled_data.csv")
    data = random.choice(CSV(HASOC_2019))
    if data["task_3"] == "UNT":
        pass
    if data["task_3"] == "TIN":
        pass
    if data["task_3"] == "NONE":
        pass
    
    if data["task_2"] == "PRFN":
        pass
    if data["task_2"] == "HATE":
        pass
    if data["task_2"] == "OFFN":
        pass
    if data["task_2"] == "NONE":
        pass
    
    if data["task_1"] == "HOF":
        pass
    if data["task_1"] == "NOT":
        pass
    data["text"] 

