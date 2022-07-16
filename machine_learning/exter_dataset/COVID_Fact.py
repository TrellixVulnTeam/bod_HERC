import os
import random
from machine_learning.exter_dataset.uitls.decode_data import load_jsonl
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/asaakyan/covidfact"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'COVID_Fact',url)


def get_data():
    COVIDFACT_dataset = get_path(dir_fs, 'COVID_Fact',"COVIDFACT_dataset.jsonl")
    data = random.choice(load_jsonl(COVIDFACT_dataset))
    # tokens, mask, c = text_encoder(data["claim"] , "Text", "unknown", None)
    # tokens, mask, c = text_encoder(data["evidence"] , "Text", "unknown", None)
    evidence = data["evidence"]
    
    if data["label"] == "REFUTED":
        pass
    elif data["label"] == "SUPPORTED":
        pass
    
    if data["flair"] == "Vaccine Research":
        pass
    elif data["flair"] == "Press Release":
        pass
    elif data["flair"] == "Preprint":
        pass
    elif data["flair"] == "Academic Report":
        pass
    elif data["flair"] == "Antivirals":
        pass
    elif data["flair"] == "Diagnostics":
        pass
    elif data["flair"] == "Epidemiology":
        pass
    # tokens, mask, c = text_encoder(data["gold_source"] , "Text", "unknown", None)
    # tokens, mask, c = text_encoder(evidence , "Text", "unknown", None)