

import os
from machine_learning.exter_dataset.uitls.decode_data import de_gz
from machine_learning.exter_dataset.uitls.download import file_download, gz_tar_download
dir_fs = os.path.dirname(os.path.realpath(__file__))


url = "https://nlp.cs.princeton.edu/SARC/"
url = "https://nlp.cs.princeton.edu/SARC/2.0/stats.json.bz2"
main_comments_url = "https://nlp.cs.princeton.edu/SARC/2.0/main/comments.json.bz2"
main_test_balanced_url = "https://nlp.cs.princeton.edu/SARC/2.0/main/test-balanced.csv.bz2"
main_test_unbalanced_url = "https://nlp.cs.princeton.edu/SARC/2.0/main/test-unbalanced.csv.bz2"
main_train_unbalanced_url = "https://nlp.cs.princeton.edu/SARC/2.0/main/train-unbalanced.csv.bz2"

pol_comments_url = "https://nlp.cs.princeton.edu/SARC/2.0/pol/comments.json.bz2"
pol_test_balanced_url = "https://nlp.cs.princeton.edu/SARC/2.0/pol/test-balanced.csv.bz2"
pol_test_unbalanced_url = "https://nlp.cs.princeton.edu/SARC/2.0/pol/test-unbalanced.csv.bz2"
pol_train_unbalanced_url = "https://nlp.cs.princeton.edu/SARC/2.0/pol/train-unbalanced.csv.bz2"
# pol_train_unbalanced_url = "https://nlp.cs.princeton.edu/SARC/2.0/raw/key.csv"

gz_tar_download(dir_fs, 'SARC',url,name="main/stats.json.bz2")
file_download(dir_fs, 'SARC',main_comments_url,name="main/comments.json.bz2")
de_gz(dir_fs,'SARC',"main/comments.json.bz2","main/comments.json")
file_download(dir_fs, 'SARC',main_test_balanced_url,name="main/test-balanced.csv.bz2")
de_gz(dir_fs,'SARC',"main/test-balanced.csv.bz2","main/test-balanced.csv")
file_download(dir_fs, 'SARC',main_test_unbalanced_url,name="main/test-unbalanced.csv.bz2")
de_gz(dir_fs,'SARC',"main/test-unbalanced.csv.bz2","main/test-unbalanced.csv")
file_download(dir_fs, 'SARC',main_train_unbalanced_url,name="main/train-unbalanced.csv.bz2")
de_gz(dir_fs,'SARC',"main/train-unbalanced.csv.bz2","main/train-unbalanced.csv")
file_download(dir_fs, 'SARC',pol_test_balanced_url,name="pol/test-balanced.csv.bz2")
de_gz(dir_fs,'SARC',"pol/test-balanced.csv.bz2","pol/test-balanced.csv")
file_download(dir_fs, 'SARC',pol_test_unbalanced_url,name="pol/test-unbalanced.csv.bz2")
de_gz(dir_fs,'SARC',"pol/test-unbalanced.csv.bz2","pol/test-unbalanced.csv")
file_download(dir_fs, 'SARC',pol_comments_url,name="pol/train-unbalanced.csv.bz2")
de_gz(dir_fs,'SARC',"pol/train-unbalanced.csv.bz2","pol/train-unbalanced.csv")


url = "https://nlp.cs.princeton.edu/SARC/"





def get_data():
    pass