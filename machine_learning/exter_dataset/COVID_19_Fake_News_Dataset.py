from machine_learning.exter_dataset.uitls.download import git_download
import os
dir_fs = os.path.dirname(os.path.realpath(__file__))
url = "https://github.com/diptamath/covid_fake_news/"
git_download(dir_fs, 'covid_fake_news',url)


def get_data():
    pass