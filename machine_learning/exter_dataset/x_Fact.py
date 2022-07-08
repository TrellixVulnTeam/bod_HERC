url = "https://github.com/utahnlp/x-fact"
import os
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.input import input_text, input_url
import numpy as np
import csv


import random

from machine_learning.exter_dataset.uitls.modle import midline, or_diff
from machine_learning.exter_dataset.uitls.output import output_bool

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'x-fact',url)

def get_data():
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
    data['link_1']
    data['evidence_1']
    # tokens, mask, c = tokenizer(data['evidence_1'], "Text", data['language'], None)
    data['language']

    data['link_2']
    data['evidence_2']
    # tokens, mask, c = tokenizer(data['evidence_2'], "Text", data['language'], None)
    data['language']

    data['link_3']
    data['evidence_3']
    # tokens, mask, c = tokenizer(data['evidence_3'], "Text", data['language'], None)
    data['language']

    data['link_4']
    data['evidence_4']
    # tokens, mask, c = tokenizer(data['evidence_4'], "Text", data['language'], None)
    data['language']

    data['link_5']
    data['evidence_5']
    # tokens, mask, c = tokenizer(data['evidence_5'], "Text", data['language'], None)
    data['language']