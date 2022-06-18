import random
from machine_learning.exter_dataset.uitls.decode_data import  load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
import os
from machine_learning.exter_dataset.uitls.input import input_twitter_post, output_classifier
from machine_learning.exter_dataset.uitls.modle import midline
url = "https://github.com/bshmueli/ReactionGIF"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ReactionGIF',url)




def get_data():
    reactionGIF = get_path(dir_fs, 'ReactionGIF',"ReactionGIF.ids.json")
    f = random.choice(load_jsonl(reactionGIF))
    out = [output_classifier(f["label"],"reaction")]
    in_ = [input_twitter_post(f["original_id"],None)]
    return midline(in_=in_,middle=out)