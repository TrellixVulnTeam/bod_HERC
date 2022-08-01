import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
import pandas as pd


from transformers import BertTokenizer
url = "https://github.com/rahulOmishra/SUMO"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'SUMO',url)
    


def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    climate_fever = get_path(dir_fs, 'SUMO', "climate_claims_raw.xlsx")
    df = pd.read_excel(climate_fever, sheet_name='Foglio1')
    datas = df.sample(1)
    for index, data in datas.iterrows():
        data["Claim"]
        data["Title"]
        data["Doc_text"]
        data["Label"]

        pass