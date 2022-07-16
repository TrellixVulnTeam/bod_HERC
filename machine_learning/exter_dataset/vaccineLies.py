url = "https://github.com/Supermaxman/vaccine-lies"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json, load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.input import input_factCheck_evidence, input_text, input_twitter_post
from machine_learning.exter_dataset.uitls.modle import midline
from machine_learning.service_scrap.modules.retrieval import Memory_Handler
try:
    dir_fs = os.path.dirname(os.path.realpath(__file__))
    git_download(dir_fs, 'vaccineLies',url)
except:
    pass


def get_data():
    db = Memory_Handler()
    paths = []
    paths.append("covid19/annotations/dev.jsonl")
    paths.append("covid19/annotations/test.jsonl")
    paths.append("covid19/annotations/train.jsonl")
    paths.append("hpv/annotations/dev.jsonl")
    paths.append("hpv/annotations/test.jsonl")
    paths.append("hpv/annotations/train.jsonl")
    hpv_misinfo = "hpv/taxonomy/misinfo.json"
    covid_misinfo = "covid19/taxonomy/misinfo.json"
    path = random.choice(paths)
    path = get_path(dir_fs, 'vaccineLies',path)
    f = random.choice(load_jsonl(path))
    misinfo = list(f['misinfo'].keys())
    evidences = []
    if "hpv" in path:
        hpv_misinfo_path = get_path(dir_fs, 'vaccineLies',hpv_misinfo)
        c = load_json(hpv_misinfo_path)
        tw = input_twitter_post(f["id"],"eng")
        for ccs in misinfo:
            text = input_text(c[ccs]['text'],"eng")
            evidence = input_factCheck_evidence(text,f['misinfo'][ccs])
            evidences.append(evidence)
    elif "covid19" in path:
        covid_misinfo_path = get_path(dir_fs, 'vaccineLies',covid_misinfo)
        c = load_json(covid_misinfo_path)
        tw = input_twitter_post(f["id"],"eng")
        for ccs in misinfo:
            text = input_text(c[ccs]['text'],"eng")
            evidence = input_factCheck_evidence(text,f['misinfo'][ccs])
            evidences.append(evidence)
    return midline(in_=[tw],middle=evidences)





def get_data():
    pass