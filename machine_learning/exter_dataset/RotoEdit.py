url = "https://github.com/isomap/factedit"
import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'factedit',url)


def get_data():
    path2 = get_path(dir_fs, 'factedit',"Dataset/RoCStories/100KStories.csv")