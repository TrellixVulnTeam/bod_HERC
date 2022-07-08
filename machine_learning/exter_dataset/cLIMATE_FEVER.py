import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
from machine_learning.exter_dataset.uitls.lalble_key import DocFactCheck
url = "https://github.com/tdiggelm/climate-fever-dataset"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'climate-fever',url)


def get_data():
    climate_fever = get_path(dir_fs, 'climate-fever', "dataset/climate-fever.jsonl")
    data = random.choice(load_jsonl(climate_fever))
    # tokens, mask, c = tokenizer(data["claim"] , "Text", "unknown", None)
    if "REFUTES" ==  data["claim_label"]:
        DocFactCheck.REFUTES
    elif "NOT_ENOUGH_INFO" == data["claim_label"]:
        DocFactCheck.NOT_ENOUGH_INFO
    elif "SUPPORTS" == data["claim_label"]:
        DocFactCheck.SUPPORTS
    for evidence in data["evidences"]:
        if "REFUTES" ==  data["evidence_label"]:
            DocFactCheck.REFUTES
        elif "NOT_ENOUGH_INFO" == data["evidence_label"]:
            DocFactCheck.NOT_ENOUGH_INFO
        elif "SUPPORTS" == data["evidence_label"]:
            DocFactCheck.SUPPORTS
        evidence["article"]
        evidence["evidence"]