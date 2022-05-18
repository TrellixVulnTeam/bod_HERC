from git import Repo
import os
url = "https://github.com/firojalam/COVID-19-disinformation"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'COVID_19_Disinfo')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
