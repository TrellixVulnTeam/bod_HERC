import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/firojalam/COVID-19-disinformation"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'COVID_19_Disinfo',url)


def get_data():
    covid19_disinfo_english_binary_dev = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_binary_dev.tsv")
    covid19_disinfo_english_binary_test = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_binary_test.tsv")
    covid19_disinfo_english_binary_train = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_binary_train.tsv")
    covid19_disinfo_english_multiclass_dev = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_multiclass_dev.tsv")
    covid19_disinfo_english_multiclass_test = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_multiclass_test.tsv")
    covid19_disinfo_english_multiclass_train = get_path(dir_fs, 'COVID_19_Disinfo',"covid19_disinfo_english_multiclass_train.tsv")