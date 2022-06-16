import os
def get_path(base_path,dataset_name,path):
    return os.path.join(base_path,"repo",dataset_name,path)