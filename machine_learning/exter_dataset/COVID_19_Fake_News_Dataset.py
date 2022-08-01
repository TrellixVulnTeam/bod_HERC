import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
import os


from transformers import BertTokenizer
from machine_learning.exter_dataset.uitls.get_path import get_path
dir_fs = os.path.dirname(os.path.realpath(__file__))
url = "https://github.com/diptamath/covid_fake_news/"
git_download(dir_fs, 'covid_fake_news',url)


def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    english_test_with_labels = get_path(dir_fs, 'covid_fake_news',"data/english_test_with_labels.csv")
    data = random.choice(CSV(english_test_with_labels))
    if data["label"] == "real":
        pass
    elif data["label"] == "fake":
        pass
    data["tweet"] 
    
    # tokens, mask, c = text_encoder(data["tweet"] , "Text", "unknown", None)
