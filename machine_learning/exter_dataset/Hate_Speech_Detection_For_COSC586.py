url =  "https://github.com/mathfather/Hate-Speech-Detection-For-COSC586"
import os
from machine_learning.exter_dataset.uitls.download import git_download


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Hate-Speech-Detection-For-COSC586',url)



def get_data():
    pass