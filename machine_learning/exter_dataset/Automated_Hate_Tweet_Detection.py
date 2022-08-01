url = "https://github.com/datascisteven/Automated-Hate-Tweet-Detection"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV, TSV, tsv_helper_triple
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
import pandas as pd


from transformers import BertTokenizer
from machine_learning.exter_dataset.uitls.lalble_key import Hate, HateOrOffensive


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Automated-Hate-Tweet-Detection',url)



def get_data():
    
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    pick = 0
    if pick == 0:
        path = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/hasoc2019_en_test-2919.tsv")
        data = TSV(path)
        data = random.choice(data)  
        
        if data["task_1"] == "HOF":
            pass
        else:
            pass
        
        if data["task_2"] == "PRFN":
            pass
        elif data["task_2"] == "HATE":
            pass
        elif data["task_2"] == "OFFN":
            pass
        
        # tokens, mask, c = tokenizer(data["text"] , "Text", "unknown", None)
    elif pick == 1:
        path = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/hasoc2020_en_train_new.xlsx")
        data = pd.read_excel(path, index_col=0)  
        
        if data["task_1"] == "HOF":
            pass
        else:
            pass
        if data["task_2"] == "PRFN":
            pass
        elif data["task_2"] == "HATE":
            pass
        elif data["task_2"] == "OFFN":
            pass
        if data["task_2"] == "TIN":
            pass
        elif data["task_2"] == "UNT":
            pass
        # tokens, mask, c = tokenizer(data["text"] , "Text", "unknown", None)
        
    elif pick == 2:
        path = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/NAACL_SRW_2016.csv")
        data = CSV(path,call =tsv_helper_triple)
        data = random.choice(data)
        
        if data[1] == "racism":
            pass
        if data[1] == "sexism":
            pass
        else:
            pass
        
        data[0]
    elif pick == 3:
        path = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/hate.csv")
        data = random.choice(CSV(path))
        
        if data["maj_label"] == "abusive":
            pass
        elif data["maj_label"] == "hateful":
            pass
        elif data["maj_label"] == "normal":
            pass
        elif data["maj_label"] == "spam":
            pass
        data["Tweet ID"] 
        data["User ID"] 
        
    elif pick == 4:
        path = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/hatespeechtwitter.csv")
        data = CSV(path)
        data = random.choice(data)
        
        if data["maj_label"] == "abusive":
            pass
        elif data["maj_label"] == "hateful":
            pass
        elif data["maj_label"] == "normal":
            pass
        data["tweet_id"]
    elif pick == 5:
        path = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/labeled_data.csv")
        data = random.choice(CSV(path))
        
        if int(data["hate_speech"]) > 0:
            pass
        if int(data["offensive_language"]) > 0:
            pass
        if int(data["neither"]) > 0:
            pass
        if int(data["class"]) > 0:
            pass
        data["tweet"] 
        
        # tokens, mask, c = tokenizer(data["tweet"] , "Text", "unknown", None)
    elif pick == 6:
        path = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/hasoc2019_en_test-2919.tsv")
        data = TSV(path)
        
        if data["task_1"] == "HOF":
            Hate.Hate
        else:
            Hate.NoHate
        
        if data["task_2"] == "PRFN":
            pass
        elif data["task_2"] == "HATE":
            pass
        elif data["task_2"] == "OFFN":
            pass
        
        if data["task_3"] == "TIN":
            pass
        elif data["task_3"] == "UNT":
            pass
        # tokens, mask, c = tokenizer(data["text"] , "Text", "unknown", None)
