url = "https://github.com/datascisteven/Automated-Hate-Tweet-Detection"
import os
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Automated-Hate-Tweet-Detection',url)



def get_data():
    df_hateful = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/df_hateful.csv")
    df_ras_sex_hate = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/df_ras_sex_hate.csv")
    hate = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/hate.csv")
    hatespeechtwitter = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/hatespeechtwitter.csv")
    hostile_sexist = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/hostile_sexist.tsv")
    labeled_data = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/labeled_data.csv")
    NAACL_SRW_2016 = get_path(dir_fs, 'Automated-Hate-Tweet-Detection',"data/original/NAACL_SRW_2016.csv")
