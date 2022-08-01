import os
import random
from git import Repo
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


from transformers import BertTokenizer
url = "https://github.com/skywalker023/focused-empathy"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'EmoCause',url)


def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    r = random.randint(0,2)
    if r == 0:
        answer_path = get_path(dir_fs, 'EmoCause',"test_a.json")
        question_path = get_path(dir_fs, 'EmoCause',"test_q.json")
    if r == 1:
        answer_path = get_path(dir_fs, 'EmoCause',"train_a.json")
        questio_pathn = get_path(dir_fs, 'EmoCause',"train_a.json")
    if r == 2:
        answer_path = get_path(dir_fs, 'EmoCause',"val_a.json")
        question_path = get_path(dir_fs, 'EmoCause',"val_q.json")
    answer_data =load_json(answer_path)
    question_data =load_json(question_path)
    answer_data = random.choice(answer_data)
    #Question
    video_name= answer_data["video_name"]
    question= answer_data["question"]
    #Answer
    for i in question_data:
        if  i["question_id"]  == answer_data["question_id"]:
            answer =i["answer"]
            type =i["type"]