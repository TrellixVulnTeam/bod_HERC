url = "https://github.com/daconjam/Harmful-LGBTQIA"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Harmful-LGBTQIA',url)



def get_data():
    reddit_comments_orientation_lgbtq_processed = get_path(dir_fs, 'Harmful-LGBTQIA',"reddit_comments_orientation_lgbtq_processed.csv")
    binary_labeled_comments = get_path(dir_fs, 'Harmful-LGBTQIA',"binary_labeled_comments.csv")
    path =random.choices([reddit_comments_orientation_lgbtq_processed,binary_labeled_comments])
    data = CSV(path)
    random.choice([data])