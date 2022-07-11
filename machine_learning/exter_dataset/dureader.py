import os
from machine_learning.exter_dataset.uitls.download import zip_download


base_path = os.path.dirname(os.path.realpath(__file__))
url = "https://aipedataset.cdn.bcebos.com/dureader/dureader_preprocessed.zip"
zip_download(base_path,"dureader",url,name="dureader_preprocessed")
url = "https://aipedataset.cdn.bcebos.com/dureader/dureader_raw.zip"
zip_download(base_path,"dureader",url,name="dureader_raw")





def get_data():
    pass