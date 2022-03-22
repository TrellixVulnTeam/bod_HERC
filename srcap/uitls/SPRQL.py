
import asyncio
import json
import os
import sys
import aiohttp
import time
from uitls.get import sem_web
sem_SPRQL = asyncio.BoundedSemaphore(300)
class SPRQL:
    def __init__(self, sparql = None, url = None, key="item") -> None:
        self.sparql = sparql
        self.url = url
        self.key = key

    async def run(self,sparql=None,i=200,session=None) -> None:
        if sparql is None:
            sparql = self.sparql
        da = {}
        async with sem_web:
            async with sem_SPRQL:
                for i in range(i):
                    a = []
                    try:
                        async with session.post(self.url, data={ 'format': 'json', 'query': sparql}) as r:
                                if r.ok:
                                    data = await r.json()
                                    ds = data["results"]["bindings"]
                                    for i in ds:
                                        item = {}
                                        for c in i.keys():
                                            item[c] = i[c]["value"]
                                        a.append(item)
                                    return a
                                else:
                                    await asyncio.sleep(10)
                                    continue
                    except  BaseException as  e:
                        print("ERROR ",type(e),":",e,":",self.url,":",sparql)
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(type(e),exc_type, fname, exc_tb.tb_lineno)
                    except:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        print("ERROR ",type(exc_obj),":",exc_obj,":",self.url,":",sparql)
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(type(e),exc_type, fname, exc_tb.tb_lineno)
                await asyncio.sleep(10)
        return []