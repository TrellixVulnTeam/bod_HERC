from git import Repo
import os

from machine_learning.exter_dataset.uitls.download import git_download
url = "https://github.com/sreyan88/toxicity-detection-in-spoken-utterances"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'deToxy-19',url)