url = "https://zenodo.org/record/3902855#.YoU4I3XMJhE"
import os
from machine_learning.exter_dataset.uitls.download import zenodo_download
dir_fs = os.path.dirname(os.path.realpath(__file__))
zenodo_download(dir_fs,"large-scale COVID-19 Twitter chatter dataset","3902855")