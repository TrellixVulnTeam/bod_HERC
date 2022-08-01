import random
from git import Repo
import os
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


from transformers import BertTokenizer
url = "https://github.com/JULIELab/EmoBank"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'emoBank',url)


def get_data():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    emoBank = get_path(dir_fs, 'emoBank',"corpus/emobank.csv")
    data = random.choice(CSV(emoBank))
    valence = data["V"]
    arousal = data["A"]
    dominance = data["D"]
    inputs = tokenizer(data["text"] , return_tensors="pt")