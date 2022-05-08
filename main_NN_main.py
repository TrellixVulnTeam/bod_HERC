import asyncio
import threading
from machine_learning.main import NN_main
from utils import asynchronous_thread_task


new_loop = asyncio.new_event_loop()
b = threading.Thread(target=asynchronous_thread_task, args=(NN_main, new_loop))
b.start()