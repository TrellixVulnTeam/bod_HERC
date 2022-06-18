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
    x = random.choice(TSV (path))
    # text input
    input_ = input_text(x['claim'],x['language'])
    # evidence
    evidence =[]
    evidence.append(or_diff(*[input_url(x['link_1']),input_text(x['evidence_1'],x['language'])]))
    evidence.append(or_diff(*[input_url(x['link_2']),input_text(x['evidence_2'],x['language'])]))
    evidence.append(or_diff(*[input_url(x['link_3']),input_text(x['evidence_3'],x['language'])]))
    evidence.append(or_diff(*[input_url(x['link_4']),input_text(x['evidence_4'],x['language'])]))
    evidence.append(or_diff(*[input_url(x['link_5']),input_text(x['evidence_5'],x['language'])]))
    output = [output_bool(x['label'],"fackcheck")]
    data = midline(in_=input_,out_=output,middle=evidence)
    # 
    
    print(data)