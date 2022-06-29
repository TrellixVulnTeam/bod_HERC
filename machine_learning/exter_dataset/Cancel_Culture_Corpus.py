url = "https://github.com/Justus-Jonas/Cancel-Culture-Corpus"
import os
import random
from machine_learning.exter_dataset.uitls.decode_data import CSV
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'Cancel-Culture-Corpus',url)



def get_data():
    alisoneroman = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/alisoneroman.csv")
    armiehammer = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/armiehammer.csv")
    bobbaffert = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/bobbaffert.csv")
    carson_king = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/carson king.csv")
    dojacat  = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/dojacat .csv")
    gabcake = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/gabcake.csv")
    ginacarano = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/ginacarano.csv")
    goya = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/goya.csv")
    jamescharles = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/jamescharles.csv")
    jimmyfallon  = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/jimmyfallon .csv")
    jk_rowling  = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/jk_rowling .csv")
    lana = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/lana.csv")
    Lin_Manuel = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/Lin_Manuel.csv")
    morgan_wallen = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/morgan wallen.csv")
    pepe_le_pew = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/pepe le pew.csv")
    pepsi = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/pepsi.csv")
    projared = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/projared.csv")
    sebastian_stan = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/sebastian stan.csv")
    seuss = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/seuss.csv")
    shane_gillis = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/shane gillis.csv")
    starbucks = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/starbucks.csv")
    UnburntWitch = get_path(dir_fs, 'Cancel-Culture-Corpus',"data/UnburntWitch.csv")
    paths = [alisoneroman,armiehammer,bobbaffert,carson_king,dojacat,gabcake,ginacarano,goya,jamescharles,jimmyfallon,jk_rowling,lana,Lin_Manuel,morgan_wallen,pepe_le_pew,pepsi,projared,sebastian_stan,seuss,shane_gillis,starbucks,UnburntWitch]
    path = random.choice(paths)
    data = random.choice(CSV(path))
    data["id"]
    data["Datetime"]
    if data["canceled"] == "False":
        pass
    elif data["canceled"] == "True":
        pass    
    if bool(data["canceled"]):
        pass
    else:
        pass
    
    if "alisoneroman" in path:
        pass
    if "armiehammer" in path:
        pass
    if "bobbaffert" in path:
        pass
    if "carson king" in path:
        pass
    if "dojacat " in path:
        pass
    if "gabcake" in path:
        pass
    if "ginacarano" in path:
        pass
    if "goya" in path:
        pass
    if "jamescharles" in path:
        pass
    if "jimmyfallon " in path:
        pass
    if "jk_rowling " in path:
        pass
    if "lana" in path:
        pass
    if "Lin_Manuel" in path:
        pass
    if "morgan wallen" in path:
        pass
    if "pepe le pew" in path:
        pass
    if "pepsi" in path:
        pass
    if "projared" in path:
        pass
    if "sebastian stan" in path:
        pass
    if "seuss" in path:
        pass
    if "shane gillis" in path:
        pass
    if "starbucks" in path:
        pass
    if "UnburntWitch" in path:
        pass