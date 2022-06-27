import os
import random
import pyarrow.parquet as pq
import pyarrow as pa
from machine_learning.exter_dataset.uitls.download import kaggle_download
from machine_learning.exter_dataset.uitls.get_path import get_path


url = "https://www.kaggle.com/datasets/uetchy/vtuber-livechat/version/34"
url2 = "https://www.kaggle.com/datasets/uetchy/vtuber-livechat-elements"

dir_fs = os.path.dirname(os.path.realpath(__file__))

# kaggle_download(dir_fs,"uetchy","vtuber-livechat-elements","test_gold.txt")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","ban_events.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-03.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-04.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-05.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-06.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-07.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-08.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-09.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-10.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-11.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2021-12.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2022-01.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2022-02.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2022-03.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2022-04.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","chats_2022-05.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","deletion_events.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-03.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-04.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-05.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-06.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-07.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-08.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-09.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-10.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-11.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2021-12.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2022-01.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2022-02.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2022-03.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2022-04.parquet")
kaggle_download(dir_fs,"uetchy","vtuber-livechat","superchats_2022-05.parquet")



def get_data():
    paths = ["ban_events.parquet","chats_2021-03.parquet","chats_2021-04.parquet","chats_2021-05.parquet","chats_2021-06.parquet","chats_2021-07.parquet","chats_2021-08.parquet","chats_2021-09.parquet","chats_2021-10.parquet","chats_2021-11.parquet","chats_2021-12.parquet","chats_2022-01.parquet","chats_2022-02.parquet","chats_2022-03.parquet","chats_2022-04.parquet","chats_2022-05.parquet","deletion_events.parquet","superchats_2021-03.parquet","superchats_2021-04.parquet","superchats_2021-05.parquet","superchats_2021-06.parquet","superchats_2021-07.parquet","superchats_2021-08.parquet","superchats_2021-09.parquet","superchats_2021-10.parquet","superchats_2021-11.parquet","superchats_2021-12.parquet","superchats_2022-01.parquet","superchats_2022-02.parquet","superchats_2022-03.parquet","superchats_2022-04.parquet","superchats_2022-05.parquet"]
    path = get_path(dir_fs, 'vtuber-livechat',random.choice(paths))
    pq_array = pa.parquet.read_table(path, memory_map=True)