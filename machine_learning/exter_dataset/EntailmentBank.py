url1 = "https://github.com/allenai/entailment_bank"
url2 = "https://drive.google.com/drive/folders/1YjjeZy9FEbXh-84-HjqOu8Rfve9oj1Te"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'EntailmentBank',url1)
# need to add google dive maybe


def get_data():
    task_1_test  = get_path(dir_fs, 'entailment_trees_emnlp2021_data_v2',"/task_1/test.jsonl")
    task_1_dev  = get_path(dir_fs, 'entailment_trees_emnlp2021_data_v2',"/task_1/dev.jsonl")
    task_1_train  = get_path(dir_fs, 'entailment_trees_emnlp2021_data_v2',"/task_1/train.jsonl")
    
    task_2_test  = get_path(dir_fs, 'entailment_trees_emnlp2021_data_v2',"/task_2/test.jsonl")
    task_2_dev  = get_path(dir_fs, 'entailment_trees_emnlp2021_data_v2',"/task_2/dev.jsonl")
    task_2_train  = get_path(dir_fs, 'entailment_trees_emnlp2021_data_v2',"/task_2/train.jsonl")
    
    task_3_test  = get_path(dir_fs, 'entailment_trees_emnlp2021_data_v2',"/task_3/test.jsonl")
    task_3_dev  = get_path(dir_fs, 'entailment_trees_emnlp2021_data_v2',"/task_3/dev.jsonl")
    task_3_train  = get_path(dir_fs, 'entailment_trees_emnlp2021_data_v2',"/task_3/train.jsonl")
    path = random.choice([task_1_test,task_1_dev,task_1_train,task_2_test,task_2_dev,task_2_train,task_3_test,task_3_dev,task_3_train])
    data = random.choice(CSV(path))
    data["context"]
    data["question"]
    data["answer"]
    data["hypothesis"]
    data["proof"]
    data["full_text_proof"]
    
    for sem in data["meta"]["add_list"]:
        sem["fact"]
    for sem in  data["meta"]["delete_list"]:
        sem["fact"]
    
    data["meta"]["sent1"]["fact"]
    data["meta"]["sent2"]["fact"]
    data["meta"]["sent3"]["fact"]
    data["meta"]["sent4"]["fact"]
    data["meta"]["sent5"]["fact"]
    data["meta"]["sent6"]["fact"]
    data["meta"]["sent7"]["fact"]
    data["meta"]["sent8"]["fact"]
    data["meta"]["sent9"]["fact"]
    data["meta"]["sent10"]["fact"]
    data["meta"]["sent11"]["fact"]
    data["meta"]["sent12"]["fact"]
    data["meta"]["sent13"]["fact"]
    data["meta"]["sent14"]["fact"]
    data["meta"]["sent15"]["fact"]
    data["meta"]["sent16"]["fact"]
    data["meta"]["sent17"]["fact"]