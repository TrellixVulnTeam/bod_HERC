import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV

from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'ClaimBuster')
os.mkdir(dir_fs)
groundtruth = "https://zenodo.org/record/3609356/files/groundtruth.csv?download=1"
crowdsourced = "https://zenodo.org/record/3609356/files/crowdsourced.csv?download=1"
all_sentences = "https://zenodo.org/record/3609356/files/all_sentences.csv?download=1"
import urllib.request
groundtrut_path = os.path.join(dir_fs,  'groundtruth.csv')
with urllib.request.urlopen(groundtruth) as f:
    text = f.read()
    with open(groundtrut_path,mode="wb") as file :
        file.write(text)
crowdsource_path = os.path.join(dir_fs, 'crowdsourced.csv')
with urllib.request.urlopen(crowdsourced) as f:
    text = f.read()
    with open(crowdsource_path,mode="wb") as file :
        file.write(text)
all_sentence_path = os.path.join(dir_fs, 'all_sentences.csv')
with urllib.request.urlopen(all_sentences) as f:
    text = f.read()
    with open(all_sentence_path,mode="wb") as file :
        file.write(text)
    


def get_data():
    path = get_path(dir_fs, 'ClaimBuster',"groundtruth.csv")
    data = random.choice(CSV(path))
    if data["Verdict"] == "-1":
        # LIE
        pass
    elif data["Verdict"] == "0":
        # True But need vaefaciomn
        pass
    elif data["Verdict"] == "1":
        # TRUE
        pass
    
    if data["Speaker_title"] == "REPUBLICAN":
        pass
    elif data["Speaker_title"] == "DEMOCRAT":
        pass
    elif data["Speaker_title"] == "INDEPENDENT":
        pass
    elif data["Speaker_title"] == "None":
        pass
    elif data["Speaker_title"] == "NULL":
        pass
    
    if data["Speaker"] =="Al Gore":
        pass
    elif data["Speaker"] =="Barack Obama":
        pass
    elif data["Speaker"] =="Bill Clinton":
        pass
    elif data["Speaker"] =="Bob Dole":
        pass
    elif data["Speaker"] =="George Bush":
        pass
    elif data["Speaker"] =="George W. Bush":
        pass
    elif data["Speaker"] =="Gerald R. Ford":
        pass
    elif data["Speaker"] =="Jimmy Carter":
        pass
    elif data["Speaker"] =="John Anderson":
        pass
    elif data["Speaker"] =="John F. Kennedy":
        pass
    elif data["Speaker"] =="John Kerry":
        pass
    elif data["Speaker"] =="John McCain":
        pass
    elif data["Speaker"] =="Michael Dukakis":
        pass
    elif data["Speaker"] =="Mitt Romney":
        pass
    elif data["Speaker"] =="Richard M. Nixon":
        pass
    elif data["Speaker"] =="Ronald Reagan":
        pass
    elif data["Speaker"] =="Ross Perot":
        pass
    elif data["Speaker"] =="Walter Mondale":
        pass
    if data["Speaker_party"] =="Former Vice President":
        pass
    elif data["Speaker_party"] =="Independent Candidate":
        pass
    elif data["Speaker_party"] =="Governor":
        pass
    elif data["Speaker_party"] =="Vice President":
        pass
    elif data["Speaker_party"] =="Congressman":
        pass
    elif data["Speaker_party"] =="Senator":
        pass
    # tokens, mask, c = tokenizer(data["Text"], "Text", "unknown", None)
    pass