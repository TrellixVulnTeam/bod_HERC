import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.decode_data import CSV, load_json
url = "https://github.com/hover-nlp/hover"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hover',url)



def get_data():
    hover_dev_release_v1 = get_path(dir_fs, 'hover',"data/hover/hover_dev_release_v1.1.json")
    hover_test_release_v1 = get_path(dir_fs, 'hover',"data/hover/hover_test_release_v1.1.json")
    hover_train_release_v1 = get_path(dir_fs, 'hover',"data/hover/hover_train_release_v1.1.json")
    hover_dev_release_v1 = load_json(hover_dev_release_v1)
    hover_test_release_v1 = load_json(hover_test_release_v1)
    hover_train_release_v1 = load_json(hover_train_release_v1)
    print(hover_test_release_v1)