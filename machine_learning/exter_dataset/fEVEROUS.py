import os
from machine_learning.exter_dataset.uitls.download import file_download, zip_download

url1 = "https://fever.ai/download/feverous/feverous_train_challenges.jsonl"
url2 = "https://fever.ai/download/feverous/feverous_dev_challenges.jsonl"
url3 = "https://fever.ai/download/feverous/feverous_test_unlabeled.jsonl"
url4 = "https://fever.ai/download/feverous/feverous-wiki-pages.zip"
url5 = "https://fever.ai/download/feverous/feverous-wiki-pages-db.zip"
base_path = os.path.dirname(os.path.realpath(__file__))
file_download(base_path,"feverous",url1,name="feverous_train_challenges.jsonl")
file_download(base_path,"feverous",url2,name="feverous_dev_challenges.jsonl")
file_download(base_path,"feverous",url3,name="feverous_test_unlabeled.jsonl")
zip_download(base_path,"feverous",url4,name="feverous-wiki-pages.zip")
zip_download(base_path,"feverous",url5,name="feverous-wiki-pages-db.zip")


def get_data():
    pass