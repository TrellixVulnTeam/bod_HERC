import os
from git import Repo
url = "https://github.com/smitp415/CSCI_544_Final_Project"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'JUSTICE')
try:
    Repo.clone_from(url,  dir_fs)
except:
    pass
repo = Repo(dir_fs)
