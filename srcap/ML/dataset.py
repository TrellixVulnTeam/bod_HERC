from torch.utils.data import Dataset
from pymongo import MongoClient
client = MongoClient()


class MultiTaskDataset(Dataset):
    def __init__(self):
        scrap = client.scrap
        self.wikidataDb = scrap.website

    def __getitem__(self, idx):
        pass
