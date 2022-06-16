import os
from machine_learning.exter_dataset.uitls.download import git_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo")
url = "https://github.com/JerryWei03/COVID-Q"
git_download(dir_fs, 'COVID-Q',url)