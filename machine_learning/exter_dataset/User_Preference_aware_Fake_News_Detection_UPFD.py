url = "https://github.com/safe-graph/GNN-FakeNews"
import os
from machine_learning.exter_dataset.uitls.download import git_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'GNN-FakeNews',url)


def get_data():
    path_train = get_path(dir_fs, 'GNN-FakeNews',"")