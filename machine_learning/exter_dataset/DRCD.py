import os
import random
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

url = "https://github.com/DRCKnowledgeTeam/DRCD"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'DRCD',url)

def get_data():
    data = random.choice( )["data"] #