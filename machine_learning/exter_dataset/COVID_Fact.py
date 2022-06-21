import os
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/asaakyan/covidfact"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'COVID_Fact',url)


def get_data():
    COVIDFACT_dataset = get_path(dir_fs, 'HASOC-2019',"COVIDFACT_dataset.jsonl")
    data = load_jsonl(COVIDFACT_dataset)
