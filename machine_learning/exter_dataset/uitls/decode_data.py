import csv
from genericpath import isfile
import gzip
import json
import os
import pickle
import tarfile
from tkinter.messagebox import RETRY
import zipfile
from os.path import isfile, join


def load_jsonl(path):
    f= []
    with open(path, 'r') as json_file:
        a = json_file.read()
        json_list = list(a.split("\n"))
    for json_str in json_list:
        try:
            f.append(json.loads(json_str))
        except:
            pass
    return f


def load_pickle (path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data

def load_json (path):
    with open(path, 'r') as f:
        data = json.loads(f.read())
    return data

def load_gzip_pickle (path):
    with gzip.open(path, 'rb') as f:
        data = pickle.load(f.read())
    return data


def load_json_pickle (path):
    with gzip.open(path, 'rb') as f:
        data = json.loads(f)
    return data

def tsv_helper_dict (file,delimiter):
    list =[]
    tsv_file = csv.reader(file, delimiter=delimiter)
    row_index = 0
    top = []
    for line in tsv_file:
        if row_index == 0:
            top=line
        else:
            data = {}
            colum_index = 0
            for cell in line:
                try:
                    data[top[colum_index]] = cell
                except:
                    pass
                colum_index = colum_index + 1
            list.append(data)
        row_index = row_index + 1
    return list



def tsv_helper_triple (file,delimiter):
    list =[]
    tsv_file = csv.reader(file, delimiter=delimiter)
    for line in tsv_file:
            data = []
            for cell in line:
                try:
                    data.append(cell)
                except:
                    pass
            list.append(data)
    return list



def de_zip(base_path,dataset_name,url,name=None):
    print("de_zip")
    zip_path = os.path.join(base_path,"repo",dataset_name,zip_path)
    output_path = os.path.join(base_path,"repo",dataset_name,output_path)
    with zipfile.ZipFile(zip_path,"r") as zip_ref:
        zip_ref.extractall(output_path)



def de_gz_tar(base_path,dataset_name,zip_path,output_path):
    print("de_gz_tar")
    zip_path = os.path.join(base_path,"repo",dataset_name,zip_path)
    output_path = os.path.join(base_path,"repo",dataset_name,output_path)
    with tarfile.open(zip_path) as zip_ref:
        zip_ref.extractall(path=output_path)

def de_gz(base_path,dataset_name,zip_path,output_path):
    print("de_gz")
    zip_path = os.path.join(base_path,"repo",dataset_name,zip_path)
    output_path = os.path.join(base_path,"repo",dataset_name,output_path)
    with gzip.open(zip_path,'rb') as fin:    
        file_content = fin.read()
        with open(output_path,mode="wb") as file :
            file.write(file_content)

def list_file(mypath):
    files =[]
    for f in os.listdir(mypath):
        file = join(mypath, f)
        if isfile(file):
            files.append(file)
    return files


def CSV (path, delimiter=",",call =tsv_helper_dict):
    with open(path) as file:
        return call(file,delimiter)

def load_gzip_CSV (path,delimiter=",",call =tsv_helper_dict):
    with gzip.open(path, 'rb') as file:
        return call(file,delimiter)

def TSV (path, delimiter="\t",call =tsv_helper_dict):
    with open(path) as file:
        return call(file,delimiter)

def load_gzip_TSV (path,delimiter="\t",call =tsv_helper_dict):
    with gzip.open(path, 'rb') as file:
        return call(file,delimiter)