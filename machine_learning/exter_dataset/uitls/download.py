import os
import tarfile
import urllib.request
import zipfile
from git import Repo
import git
from kaggle.api.kaggle_api_extended import KaggleApi
from datasets import load_dataset
from __future__ import print_function
import os.path
import io
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

try:
    from kaggle import KaggleApi
    api = KaggleApi()
    api.authenticate()
except:
    api =None

try:
    from mumin import MuminDataset
except:
    api =None

def zip_download(base_path,dataset_name,url,name=None):
    if name is not None:
        dir_name = os.path.join(base_path,"repo",dataset_name)
        zip_name = os.path.join(base_path,"repo",dataset_name,name+".zip")
    else:
        zip_name = os.path.join(base_path,"repo",dataset_name,dataset_name+".zip")
        dir_name = os.path.join(base_path,"repo",dataset_name)
    
    if os.path.isdir(dir_name) and os.path.exists(dir_name):
        if len(os.listdir(dir_name)) != 0:
            return
    else:
        os.mkdir(dir_name)
    
    if not os.path.exists(zip_name):
        with urllib.request.urlopen(url) as f:
            text = f.read()
            with open(zip_name,"wb") as file :
                file.write(text)
    
    try:
        with zipfile.ZipFile(zip_name,"r") as zip_ref:
            zip_ref.extractall(dir_name)
    except:
        print("zip_download cant unzip:",dataset_name)



def gz_tar_download(base_path,dataset_name,url,name=None):
    if name is not None:
        dir_name = os.path.join(base_path,"repo",dataset_name)
        zip_name = os.path.join(base_path,"repo",dataset_name,dataset_name+".gz_tar")
    else:
        zip_name = os.path.join(base_path,"repo",dataset_name,dataset_name+".gz_tar")
        dir_name = os.path.join(base_path,"repo",dataset_name)
    
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    try:
        dir = os.listdir(dir_name)
        if len(dir) != 0:
            return
    except:
        pass
    if not os.path.exists(zip_name):
        with urllib.request.urlopen(url) as f:
            text = f.read()
            with open(zip_name,mode="wb") as file :
                file.write(text)
    with tarfile.open(zip_name) as zip_ref:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(zip_ref, path=dir_name)

def git_download(base_path,dataset_name,url):
    
    dir_name = os.path.join(base_path,"repo",dataset_name)
    
    
    if os.path.isdir(dir_name) and os.path.exists(dir_name):
        if len(os.listdir(dir_name)) != 0:
            return
    else:
        os.mkdir(dir_name)
    print("download git")
    Repo.clone_from(url, dir_name)

def kaggle_download(base_path,dataset_name,name):
    path = os.path.join(base_path,"repo",dataset_name, name)
    try:
        api.dataset_download_files(name,path=path, unzip=True)
    except:
        pass

def huggingface_download(base_path,dataset_name,name,subname):
    dir_fs = os.path.join(base_path,"repo", dataset_name)
    if not os.path.isdir(dir_fs):
        os.mkdir(dir_fs)
    try:
        dataset = load_dataset(name, subname,data_dir=dir_fs)
    except:
        print("fail huggingface_download:",dataset_name)
    return dataset

def zenodo_download(base_path,dataset_name,id_zenodo):
    from zenodo_client import Zenodo
    dir_fs = os.path.join(base_path,"repo", dataset_name)
    
    if not os.path.isdir(dir_fs):
        os.mkdir(dir_fs)
    
    dir = os.listdir(dir_fs)
    if len(dir) != 0:
        return
    try:
        zenodo = Zenodo()
        dataset = zenodo.download_latest(id_zenodo, path=dir_fs)
    except:
        pass
    return dataset

def drive_google_download(base_path,dataset_name,id_google_dive):
    pass
def onedrive_download(base_path,dataset_name,id_zenodo):
    pass
def dataverse_download(base_path,dataset_name,id_zenodo):
    pass
def mumin_download(base_path,dataset_name,size):
    bearer_token = ""
    dataset = MuminDataset(bearer_token, size='small')

def file_download(base_path,dataset_name,url,name=None,ext=None):
    dir_name = os.path.join(base_path,"repo",dataset_name)
    if name is not None:
        path_name = os.path.join(base_path,"repo",dataset_name, name)
    elif ext is not None:
        path_name = os.path.join(base_path,"repo",dataset_name,dataset_name+"."+ext)
    else:
        path_name = os.path.join(base_path,"repo",dataset_name,dataset_name)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    if not os.path.isdir(path_name) and os.path.exists(path_name):
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
    dir_name = os.path.join(base_path,"repo",dataset_name)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    dir_name = os.path.join(base_path,"repo",dataset_name,file_name)
    if  os.path.isdir(dir_name) and os.path.exists(dir_name):
        text= api.datasets_download_file(user,dataset_name,file_name=file_name)
        with open(dir_name,mode="wb") as file :
                file.write(text)

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']



def google_download_file(base_path,dataset_name,real_file_id,file_name):
    dir_name = os.path.join(base_path,"repo",dataset_name)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    file_path = os.path.join(base_path,"repo",dataset_name,file_name)
    if not os.path.isdir(file_path) and os.path.exists(file_path):
        return False
    creds, _ = google.auth.default()

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_id = real_file_id

        # pylint: disable=maybe-no-member
        request = service.files().get_media(fileId=file_id)
        with open(file_path, 'w') as file:
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(F'Download {int(status.progress() * 100)}.')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.getvalue()

def download_googledrive_folder():
        # create drive api client
        pass
creds, _ = google.auth.default()
service = build('drive', 'v3', credentials=creds)
resource = service.files()
