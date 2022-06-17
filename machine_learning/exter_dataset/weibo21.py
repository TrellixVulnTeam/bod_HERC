url = "https://github.com/kennqiang/MDFEND-Weibo21"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_pickle
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'MDFEND-Weibo21',url)

def get_data():
    paths = []
    paths.append("MDFEND-Weibo21/data/test.pkl")
    paths.append("MDFEND-Weibo21/data/train.pkl")
    paths.append("MDFEND-Weibo21/data/val.pkl")
    path = get_path(dir_fs, 'x-fact',random.choice(paths))
    c = load_pickle (path)
    print(c)