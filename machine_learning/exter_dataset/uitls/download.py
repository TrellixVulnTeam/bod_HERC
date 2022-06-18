import os
import tarfile
import urllib.request
import zipfile
from git import Repo
from kaggle.api.kaggle_api_extended import KaggleApi
from datasets import load_dataset

try:
    from kaggle import KaggleApi
    api = KaggleApi()
    api.authenticate()
except:
    api =None

try:
    from mumin import MuminDataset
    dataset = MuminDataset(bearer_token, size='small')
except:
    api =None

def zip_download(base_path,dataset_name,url,name=None):
    print("zip_download:",dataset_name)
    if name is not None:
        dir_name = os.path.join(base_path,"repo",dataset_name)
        zip_name = os.path.join(base_path,"repo",dataset_name,name+".zip")
    else:
        zip_name = os.path.join(base_path,"repo",dataset_name,dataset_name+".zip")
        dir_name = os.path.join(base_path,"repo",dataset_name)
    try:
        print(dir_name)
        os.mkdir(dir_name)
    except:
        pass
    with urllib.request.urlopen(url) as f:
        text = f.read()
        with open(zip_name,"wb") as file :
            file.write(text)
    with zipfile.ZipFile(zip_name,"r") as zip_ref:
        zip_ref.extractall(dir_name)



def gz_tar_download(base_path,dataset_name,url,name=None):
    print("gz_tar_download:",dataset_name)
    if name is not None:
        dir_name = os.path.join(base_path,"repo",dataset_name)
        zip_name = os.path.join(base_path,"repo",dataset_name,dataset_name+".gz_tar")
    else:
        zip_name = os.path.join(base_path,"repo",dataset_name,dataset_name+".gz_tar")
        dir_name = os.path.join(base_path,"repo",dataset_name)
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

def git_download(base_path,dataset_name,url):
    print("git_download:",dataset_name)
    dir_name = os.path.join(base_path,"repo",dataset_name)
    try:
        os.mkdir(dir_name)
    except:
        pass
    try:
        Repo.clone_from(url, dir_name)
    except:
        pass


def kaggle_download(base_path,dataset_name,name):
    print("kaggle_download:",dataset_name)
    path = os.path.join(base_path,"repo",dataset_name, name)
    api.dataset_download_files(name,path=path, unzip=True)
    print("kaggle_done")

def huggingface_download(base_path,dataset_name,name,subname):
    print("huggingface_download:",dataset_name)
    dir_fs = os.path.join(base_path,"repo", dataset_name)
    os.mkdir(dir_fs)
    dataset = load_dataset(name, subname,data_dir=dir_fs)
    return dataset

def zenodo_download(base_path,dataset_name,id_zenodo):
    print("zenodo_download:",dataset_name)
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
    print("drive_google_download")
    pass
def onedrive_download(base_path,dataset_name,id_zenodo):
    pass
def dataverse_download(base_path,dataset_name,id_zenodo):
    pass
def mumin_download(base_path,dataset_name,id_zenodo):
    pass
def file_download(base_path,dataset_name,url,name=None,ext=None):
    print("file_download:",dataset_name)
    dir_name = os.path.join(base_path,"repo",dataset_name)
    if name is not None:
        path_name = os.path.join(base_path,"repo",dataset_name, name)
    elif ext is not None:
        path_name = os.path.join(base_path,"repo",dataset_name,dataset_name+"."+ext)
    else:
        path_name = os.path.join(base_path,"repo",dataset_name,dataset_name)
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
    print("kaggle_download",dataset_name)
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
