import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, list_file
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/kinit-sk/medical-misinformation-dataset"

dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'medical-misinformation-dataset',url)

def get_data():
    mphasis = get_path(dir_fs, 'medical-misinformation-dataset',"mphasis/sample_data")
    paths = list_file(mphasis)
    path = random.choice(paths)
    data = random.choice(CSV(path))
    # tokens, mask, c = tokenizer(data["statement"], "Text", data['language'], None)
    data["rating"]
