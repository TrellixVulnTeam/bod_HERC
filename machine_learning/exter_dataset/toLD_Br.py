import os
import random
from sysconfig import get_path
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.service_scrap.modules.text import text_encoder
from transformers import BertTokenizer
url = "https://github.com/JAugusto97/ToLD-Br"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ToLD-Br',url)


def get_data():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    path = get_path(dir_fs, 'ToLD-Br',"ToLD-BR_alpha.csv")
    data = random.choice(CSV(path))
    boolen_homophobia = False
    boolen_insult = False
    boolen_racism = False
    boolen_obscene = False
    boolen_xenophobia = False
    if data["homophobia"] == "1.0":
        boolen_homophobia = True
    if data["obscene"] == "1.0":
        boolen_insult = True
    if data["insult"] == "1.0":
        boolen_racism = True
    if data["racism"] == "1.0":
        boolen_obscene = True
    if data["xenophobia"] == "1.0":
        boolen_xenophobia = True
    inputs = tokenizer(data["text"], return_tensors="pt")
    return {
        "input":inputs,
        "boolen_homophobia":boolen_homophobia,
        "boolen_insult":boolen_insult,
        "boolen_racism":boolen_racism,
        "boolen_obscene":boolen_obscene,
        "boolen_xenophobia":boolen_xenophobia
    }
    