url = "https://github.com/alessandrocuda/ReSt"
import os
from machine_learning.exter_dataset.uitls.decode_data import TSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'ReSt',url)

def get_data():
    path1 = get_path(dir_fs, 'ReSt',"dataset/haspeede2/preprocessed/dev/dev.json")
    path2 = get_path(dir_fs, 'ReSt',"dataset/haspeede2/preprocessed/reference/reference_news.csv")
    data1 = TSV(path1)
    data2 = TSV(path2)