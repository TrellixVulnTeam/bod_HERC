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
    if data["label"] == "partly true/misleading":
        pass
    elif data["label"] == "mostly true":
        pass
    elif data["label"] == "mostly false":
        pass
    elif data["label"] == "true":
        pass
    elif data["label"] == "false":
        pass
    data['language']
    data['site']
    data['claim']
    # tokens, mask, c = tokenizer(data['claim'], "Text", data['language'], None)
    # evidence
    text = load_url(data['link_1'])
    db.hash_add(value=data['evidence_1'],mode = "TEXT", language = data['language'])

    text = load_url(data['link_2'])
    data['language']
    db.hash_add(value=data['evidence_2'],mode = "TEXT", language = data['language'])

    text = load_url(data['link_3'])
    # tokens, mask, c = tokenizer(data['evidence_3'], "Text", data['language'], None)
    data['language']
    db.hash_add(value=data['evidence_3'],mode = "TEXT", language = data['language'])

    text = load_url(data['link_4'])
    # tokens, mask, c = tokenizer(data['evidence_4'], "Text", data['language'], None)
    db.hash_add(value=data['evidence_4'],mode = "TEXT",type="TEXT", language = data['language'])

    text = load_url(data['link_5'])
    # tokens, mask, c = tokenizer(data['evidence_5'], "Text", data['language'], None)
    db.hash_add(value=data['evidence_5'],mode = "TEXT", language = data['language'])