import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import file_download, zip_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.service_scrap.modules.retrieval import Memory_Handler

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
    db = Memory_Handler()
    train  = get_path(base_path, 'EntailmentBank',"train.jsonl")
    shared_task_dev  = get_path(base_path, 'EntailmentBank',"shared_task_dev.jsonl")
    shared_task_test  = get_path(base_path, 'EntailmentBank',"shared_task_test.jsonl")
    path = random.choice([train,shared_task_dev,shared_task_test])
    data = random.choice(load_jsonl(path))
    data["id"]
    data["verifiable"]
    data["label"]
    data["claim"]
    data["evidence"]