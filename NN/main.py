
import random
from torch.utils.data import Dataset, DataLoader
from service_scrap.service import Getdata, do_toplevel
from service_scrap.service import do_someting
from service_scrap.service import get_scrape_wheres
from service_scrap.data_pull.wikidata import wikidata_extact
from service_scrap.service import scrape_types


for i in Getdata():
    print(i)
