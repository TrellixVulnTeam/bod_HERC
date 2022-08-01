import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.service.twitter import tweet_downloader
from transformers import BertTokenizer
url = "https://github.com/gabll/some-like-it-hoax"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'some_Like_it_Hoax',url)



def get_data():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    path = get_path(dir_fs, 'some_Like_it_Hoax',"EDA/hoaxpagedict.json")
    data = load_json(path)
    key = random.choice(data.keys())
    if data[key] == "true":
        boolen_Hoax = True
    elif data[key] == "false":
        boolen_Hoax = False
    # twitter id 
    text = tweet_downloader(key)
    inputs = tokenizer(text, return_tensors="pt")
    return {
        "input":inputs,
        "boolen_Hoax":boolen_Hoax
    }