url = "https://github.com/utahnlp/x-fact"
import os
from machine_learning.data_url import load_url
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.input import input_text, input_url
import numpy as np
import csv


import random

from machine_learning.exter_dataset.uitls.modle import midline, or_diff
from machine_learning.exter_dataset.uitls.output import output_bool
from machine_learning.service_scrap.modules.retrieval import Memory_Handler

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'x-fact',url)

value_4_factCheck = ["False", "Mostly false",
                     "Half true", "Mostly true", "True"]


def get_data():
    db = Memory_Handler()
    paths = []
    paths.append("data/x-fact/dev.all.tsv")
    paths.append("data/x-fact/ood.tsv")
    paths.append("data/x-fact/test.all.tsv")
    paths.append("data/x-fact/train.all.tsv")
    paths.append("data/x-fact/zeroshot.tsv")
    
    paths.append("data/x-fact-including-en/dev.all.tsv")
    paths.append("data/x-fact-including-en/ood.tsv")
    paths.append("data/x-fact-including-en/test.all.tsv")
    paths.append("data/x-fact-including-en/train.all.tsv")
    paths.append("data/x-fact-including-en/zeroshot.tsv")
    path = get_path(dir_fs, 'x-fact',random.choice(paths))
    data = random.choice(TSV (path))
    ## FACT CHECK
    fact_check = 0
    if data["label"] == "partly true/misleading":
        fact_check = 2
    elif data["label"] == "mostly true":
        fact_check = 3
    elif data["label"] == "mostly false":
        fact_check = 1
    elif data["label"] == "true":
        fact_check = 4
    elif data["label"] == "false":
        fact_check = 0
    inputs = data['claim']
    
    text = load_url(data['link_1'])
    db.hash_add(text,data['link_1'],type = "web", lang = data['language'])
    text = load_url(data['link_2'])
    db.hash_add(text,data['link_2'],type = "web", lang = data['language'])
    text = load_url(data['link_3'])
    db.hash_add(text,data['link_3'],type = "web", lang = data['language'])
    text = load_url(data['link_4'])
    db.hash_add(text,data['link_4'],type = "web", lang = data['language'])
    text = load_url(data['link_5'])
    db.hash_add(text,data['link_5'],type = "web", lang = data['language'])
    return {
        "db":db,
        "language":data['language'],
        "input":inputs,
        "boolen_toxicity":fact_check
    }
