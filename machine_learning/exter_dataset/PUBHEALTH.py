import os
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


url = "https://github.com/neemakot/Health-Fact-Checking"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Health-Fact-Checking',url)




def get_data():
    dev_dataset = get_path(dir_fs, 'Health-Fact-Checking/data/PUBHEALTH',"dev.tsv")
    dev_dataset = get_path(dir_fs, 'Health-Fact-Checking/data/PUBHEALTH',"test.tsv")
    dev_dataset = get_path(dir_fs, 'Health-Fact-Checking/data/PUBHEALTH',"train.tsv")
    data = CSV(dev_dataset)
    explanation= data["explanation"]
    main_text=data["main_text"]
    sources=data["sources"]
    if data["lable"] == "mixture":
        pass
    if data["lable"] == "unproven":
        pass
    if data["lable"] == "true":
        pass
    if data["lable"] == "false":
        pass

    pass
    
    # tokens, mask, c = tokenizer(data["claim"] "Text", "unknown", None)
    # tokens, mask, c = tokenizer(data["explanation"] "Text", "unknown", None)
    # tokens, mask, c = tokenizer(data["main_text"] "Text", "unknown", None)
