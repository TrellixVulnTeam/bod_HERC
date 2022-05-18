import os
from git import Repo
url = "https://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/bioclaim/"
dir_fs = os.path.dirname(os.path.realpath(__file__))
dir_fs = os.path.join(dir_fs, "repo", 'coVERT')
Repo.clone_from(url,  dir_fs)
repo = Repo(dir_fs)
