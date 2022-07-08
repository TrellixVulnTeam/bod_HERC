url = "https://github.com/victorknox/Hate-Speech-Detection-in-Hindi"
import os
import random 
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Hate-Speech-Detection-in-Hindi',url)



def get_data():
    test_dataset_path = get_path(dir_fs, 'Hate-Speech-Detection-in-Hindi',"Dataset/test.csv")
    train_dataset_path = get_path(dir_fs, 'Hate-Speech-Detection-in-Hindi',"Dataset/train.csv")
    valid_dataset_path = get_path(dir_fs, 'Hate-Speech-Detection-in-Hindi',"Dataset/valid.csv")
    test_dataset_csv = CSV(random.choice([test_dataset_path,train_dataset_path,valid_dataset_path]))
    test_dataset_csv["Post"]
    labels = []
    for label in test_dataset_csv["Labels Set"].split(","):
        labels.append(label)
    # tokens, mask, c = tokenizer(test_dataset_csv["Post"] , "Text", "unknown", None)