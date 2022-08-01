
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
import os
url = "https://github.com/moinnadeem/stereoset.git"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'stereoSet',url)


def get_data():
    # mask == BLANK
    # sill need to do
    path = get_path(dir_fs, 'stereoSet',"data/dev.json")
    data = load_json(path)
    data = random.choice(data["data"]["intersentence"])
    if data["bias_type"] == "race":
        pass
    if data["bias_type"] == "profession":
        pass
    if data["bias_type"] == "gender":
        pass
    
    # tokens, mask, c = tokenizer(data["context"], "Text", data['language'], None)

    for sentence in data["sentences"]:
        pass