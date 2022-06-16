import os
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
all_sentence_path = os.path.join(dir_fs,  'all_sentences.csv')
with urllib.request.urlopen(all_sentences) as f:
    text = f.read()
    with open(all_sentence_path,mode="wb") as file :
        file.write(text)
    