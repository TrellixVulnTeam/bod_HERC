import os
import random
from sysconfig import get_path
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/JAugusto97/ToLD-Br"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ToLD-Br',url)


def get_data():
        path = get_path(dir_fs, 'ToLD-Br',"ToLD-BR_alpha.csv")
        data = random.choice(CSV(path))
        # tokens, mask, c = tokenizer(data["text"], "Text", data['language'], None)
        if data["homophobia"] == "1.0":
            pass
        else:
            pass
        if data["obscene"] == "1.0":
            pass
        else:
            pass
        if data["insult"] == "1.0":
            pass
        else:
            pass
        if data["racism"] == "1.0":
            pass
        else:
            pass
        if data["xenophobia"] == "1.0":
            pass
        else:
            pass