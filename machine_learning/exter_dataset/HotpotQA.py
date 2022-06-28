import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_json
from machine_learning.exter_dataset.uitls.download import file_download
from machine_learning.exter_dataset.uitls.get_path import get_path

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
    hotpot_dev_distractor = get_path(dir_fs, 'hotpot',"hotpot_dev_distractor_v1.json")
    hotpot_dev_fullwiki = get_path(dir_fs, 'hotpot',"hotpot_dev_fullwiki_v1.json")
    hotpot_test_fullwiki = get_path(dir_fs, 'hotpot',"hotpot_test_fullwiki_v1.json")
    hotpot_train = get_path(dir_fs, 'hotpot',"hotpot_train_v1.1.json")
    json_hotpot_dev_distractor =load_json(random.choice([hotpot_test_fullwiki,hotpot_dev_fullwiki,hotpot_dev_distractor,hotpot_train]))
    print(json_hotpot_dev_distractor)

    pass