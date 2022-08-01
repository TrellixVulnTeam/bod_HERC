from machine_learning.exter_dataset.uitls.decode_data import TSV, tsv_helper_triple
from machine_learning.exter_dataset.uitls.download import  zip_download
import os
import random
from machine_learning.exter_dataset.uitls.get_path import get_path
from transformers import BertTokenizer
url = "https://www.cs.ucsb.edu/~william/data/liar_dataset.zip"
dir_fs = os.path.dirname(os.path.realpath(__file__))
zip_download(dir_fs,"liar_dataset",url)



def get_data():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    test_dataset = get_path(dir_fs, 'liar_dataset',"test.tsv")
    train_dataset = get_path(dir_fs, 'liar_dataset',"train.tsv")
    valid_dataset = get_path(dir_fs, 'liar_dataset',"valid.tsv")
    path = random.choice([test_dataset,train_dataset,valid_dataset])
    data = random.choice(TSV(path,call=tsv_helper_triple))
    if data[1] == "true":
        fact_check = 4
    elif data[1] == "barely-true":
        fact_check = 2
    elif data[1] == "half-true":
        fact_check = 3
    elif data[1] == "false":
        fact_check = 1
    elif data[1] == "pants-fire":
        fact_check = 0
    inputs = tokenizer(data[2], return_tensors="pt")
    return {
        "language":data['language'],
        "input":inputs,
        "4_factCheck":fact_check
    }
    