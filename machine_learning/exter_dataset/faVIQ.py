import random
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import file_download, zip_download
import os

from machine_learning.exter_dataset.uitls.get_path import get_path

urls_a_zip = "https://nlp.cs.washington.edu/ambigqa/data/faviq_a_set_v1.2.zip"
urls_b_zip = "https://nlp.cs.washington.edu/ambigqa/data/faviq_r_set_v1.2.zip"
url_wiki = "https://nlp.cs.washington.edu/ambigqa/data/wikipedia_20190801.jsonl"
urlc_a_zip = "https://nlp.cs.washington.edu/ambigqa/data/fact_correction_a_set.zip"
urlc_b_zip = "https://nlp.cs.washington.edu/ambigqa/data/fact_correction_r_set.zip"

dir_fs = os.path.dirname(os.path.realpath(__file__))
file_download(dir_fs,"faviq",url_wiki,name="faviq_a_set_v1.jsonl")
zip_download(dir_fs,"faviq",urls_a_zip,name="faviq_a_set_v1.2")
zip_download(dir_fs,"faviq",urls_b_zip,name="faviq_r_set_v1.2")
zip_download(dir_fs,"faviq",urlc_a_zip,name="fact_correction_a_set")
zip_download(dir_fs,"faviq",urlc_b_zip,name="fact_correction_r_set")


def get_data():
    train  = get_path(dir_fs, 'faviq',"faviq_a_set_v1.jsonl")
    path = random.choice([train])
    data = random.choice(load_jsonl(path))