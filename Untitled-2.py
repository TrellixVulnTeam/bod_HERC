from machine_learning.service_scrap.modules.retrieval import Retrieval, Hashing
import torch
import machine_learning.service_scrap.modules.variables as variables
from machine_learning.service_scrap.modules.text import TextEncoder


xss = Hashing()
text ="""
A: haven’t looked much into it, the price of the drives themselves puts me off at around £20.

B: from what I can tell it doesn’t make much difference if at all, just means you need to install priiloader if you want brick protection, which you should do regardless
"""
xss(text,mode="TEXT",lang="en",type_="TEXT")