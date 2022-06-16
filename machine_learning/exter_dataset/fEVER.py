import os
from machine_learning.exter_dataset.uitls.download import file_download, zip_download

url1 = "https://fever.ai/download/fever/train.jsonl"
url2 = "https://fever.ai/download/fever/shared_task_dev.jsonl"
url3 = "https://fever.ai/download/fever/shared_task_test.jsonl"
url4 = "https://fever.ai/download/fever/wiki-pages.zip"

base_path = os.path.dirname(os.path.realpath(__file__))
file_download(base_path,"fever",url1,name="train.jsonl")
file_download(base_path,"fever",url2,name="shared_task_dev.jsonl")
file_download(base_path,"fever",url3,name="shared_task_test.jsonl")
zip_download (base_path,"fever",url4,name="wiki-pages.zip")


def get_data():
    pass