import os
import tarfile
import urllib.request
import zipfile
from git import Repo
from kaggle.api.kaggle_api_extended import KaggleApi
from datasets import load_dataset

from kaggle import KaggleApi
api = KaggleApi()
api.authenticate()

def zip_download(base_path,dataset_name,url,name=None):
    if name is not None:
        zip_name = os.path.join(base_path,"repo",dataset_name, name+".zip")
        dir_name = os.path.join(base_path,"repo",dataset_name, name)
    else:
        zip_name = os.path.join(base_path,"repo",dataset_name,dataset_name+".zip")
        dir_name = os.path.join(base_path,"repo",dataset_name,dataset_name)
    try:
        os.mkdir(dir_name)
    except:
        pass
    with urllib.request.urlopen(url) as f:
        text = f.read()
        with open(zip_name,"wb") as file :
            file.write(text)
    with zipfile.ZipFile(zip_name,"r") as zip_ref:
        zip_ref.extractall(dir_name)

def git_download(base_path,dataset_name,url):
    dir_name = os.path.join(base_path,"repo",dataset_name)
    try:
        os.mkdir(dir_name)
    except:
        pass
    try:
        Repo.clone_from(url, dir_name)
    except:
        pass


def gz_tar_download(base_path,dataset_name,url,name=None):
    if name is not None:
        zip_name = os.path.join(base_path,"repo",dataset_name, name+".zip")
        dir_name = os.path.join(base_path,"repo",dataset_name, name)
    else:
        zip_name = os.path.join(base_path,"repo",dataset_name,dataset_name+".zip")
        dir_name = os.path.join(base_path,"repo",dataset_name,dataset_name)
    try:
        os.mkdir(dir_name)
    except:
        pass
    with urllib.request.urlopen(url) as f:
        text = f.read()
        with open(zip_name,mode="wb") as file :
            file.write(text)
    with tarfile.open(zip_name) as zip_ref:
        zip_ref.extractall(path=dir_name)


def kaggle_download(base_path,dataset_name,name):
    path = os.path.join(base_path,"repo",dataset_name, name)
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(name,path=path, unzip=True)

def huggingface_download(base_path,dataset_name,name,subname):
    dir_fs = os.path.join(base_path,"repo", dataset_name)
    os.mkdir(dir_fs)
    dataset = load_dataset(name, subname,data_dir=dir_fs)
    return dataset

def zenodo_download(base_path,dataset_name,id_zenodo):
    from zenodo_client import Zenodo
    dir_fs = os.path.join(base_path,"repo", dataset_name)
    try:
        os.mkdir(dir_fs)
    except:
        pass
    zenodo = Zenodo()
    dataset = zenodo.download_latest(id_zenodo, path=dir_fs)
    return dataset

def drive_google_download(base_path,dataset_name,id_google_dive):
    pass
def onedrive_download(base_path,dataset_name,id_zenodo):
    pass
def dataverse_download(base_path,dataset_name,id_zenodo):
    pass
def mumin_download(base_path,dataset_name,id_zenodo):
    pass
def file_download(base_path,dataset_name,url,name=None,ext=None):
    dir_name = os.path.join(base_path,"repo",dataset_name)
    if name is None:
        path_name = os.path.join(base_path,"repo",dataset_name, name)
    elif ext is None:
        path_name = os.path.join(base_path,"repo",dataset_name,dataset_name+"."+ext)
    else:
      raise "need name and ext"  
    try:
        os.mkdir(dir_name)
    except:
        pass
    with urllib.request.urlopen(url) as f:
        text = f.read()
        with open(path_name,mode="wb") as file :
            file.write(text)

def drive_google_download(base_path,dataset_name,url):
    pass

def one_drive_download(base_path,dataset_name,url):
    pass

def dataverse_download(base_path,dataset_name,url):
    pass

def mumin_download(base_path,dataset_name,url):
    pass
def dropbox_download(base_path,dataset_name,url):
    pass


def kaggle_download(base_path,user,dataset_name,file_name):
    try:
        dir_name = os.path.join(base_path,"repo",dataset_name)
        os.mkdir(dir_name)
    except:
        pass
    dir_name = os.path.join(base_path,"repo",dataset_name,file_name)
    print(dir_name)
    text= api.datasets_download_file(user,dataset_name,file_name=file_name)
    with open(dir_name,mode="wb") as file :
            file.write(text)




# from kaggle import KaggleApi
# from kaggle.models.kaggle_models_extended import ListFilesResult
# api = KaggleApi()
# api.authenticate()
# a = api.datasets_list_files_with_http_info(owner_slug="uetchy",dataset_slug="vtuber-livechat-elements")

# dataset_list_files_result = api.process_response(a)
# result = ListFilesResult(dataset_list_files_result)
# print(result.error_message)
# for file in result.files:
#     print(file)