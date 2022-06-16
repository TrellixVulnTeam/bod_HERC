import os
from machine_learning.exter_dataset.uitls.download import file_download

url_hotpot_train_v1 = "http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_train_v1.1.json"
url_hotpot_dev_distractor_v1 = "http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_dev_distractor_v1.json"
url_hotpot_dev_fullwiki_v1 = "http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_dev_fullwiki_v1.json"
url_hotpot_test_fullwiki_v1 = "http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_test_fullwiki_v1.json"
dir_fs = os.path.dirname(os.path.realpath(__file__))
file_download(dir_fs,"hotpot",url_hotpot_train_v1,name="hotpot_train_v1.1.json")
file_download(dir_fs,"hotpot",url_hotpot_dev_distractor_v1,name="hotpot_dev_distractor_v1.json")
file_download(dir_fs,"hotpot",url_hotpot_dev_fullwiki_v1,name="hotpot_dev_fullwiki_v1.json")
file_download(dir_fs,"hotpot",url_hotpot_test_fullwiki_v1,name="hotpot_test_fullwiki_v1.json")


def get_data():
    pass