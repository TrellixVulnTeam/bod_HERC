
import asyncio
from torch.utils.data import Dataset, DataLoader
from machine_learning.service_scrap.service import Getdata


local_loop = None


async def NN_main(name):
    async for data in Getdata():
        continue
        # print(data)
