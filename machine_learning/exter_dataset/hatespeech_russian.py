url  = "https://github.com/Aniezka/hatespeech-russian"
import os
from machine_learning.exter_dataset.uitls.decode_data import de_zip
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'hatespeech-russian',url)
de_zip(dir_fs, 'hatespeech-russian',"data/chatbots_dataset_final.csv.zip" )

def get_data():
    pass