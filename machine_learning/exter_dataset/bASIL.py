import os
import random
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path
url = "https://github.com/marshallwhiteorg/emnlp19-media-bias"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'emnlp19-media-bias',url)


def get_data():
    path_articles_2010 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2010")
    path_articles_2011 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2011")
    path_articles_2012 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2012")
    path_articles_2013 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2013")
    path_articles_2014 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2014")
    path_articles_2015 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2015")
    path_articles_2016 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2016")
    path_articles_2017 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2017")
    path_articles_2018 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2018")
    path_articles_2019 = get_path(dir_fs, 'Table-Fact-Checking',"annotations/articles/2019")
    paths = [path_articles_2010,path_articles_2011,path_articles_2012,path_articles_2013,path_articles_2014,path_articles_2015,path_articles_2016,path_articles_2017,path_articles_2018,path_articles_2019]
    path = random.choice(paths)