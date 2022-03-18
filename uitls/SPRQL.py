
import asyncio
import json
import os
import sys
import aiohttp
import time
from uitls.get import sem_web
sem_SPRQL = asyncio.BoundedSemaphore(4)
class SPRQL:
    def __init__(self, sparql = None, url = None, key="item") -> None:
        self.sparql = sparql
        self.url = url
        self.key = key

    async def run(self,sparql=None,i=10) -> None:
        if sparql is None:
            sparql = self.sparql
        da = {}
        async with sem_web:
            async with sem_SPRQL:
                for i in range(i):
                    a = []
                    try:
                        c = aiohttp.TCPConnector(enable_cleanup_closed=False,use_dns_cache=False)
                        async with aiohttp.ClientSession(connector=c) as session:
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
                                    for header in  r.headers:
                                        if "Retry-After" == header[0]:
                                            try:
                                                after = int(header[1])
                                            except:
                                                after = 10
                                            break
                                    else:
                                        after = 10
                                    await asyncio.sleep(after)
                                    continue
                    except KeyboardInterrupt as k:
                        exit()
                    except  json.decoder.JSONDecodeError as  e:
                                    await asyncio.sleep(after)
                    except  aiohttp.ClientPayloadError as  e:
                                    await asyncio.sleep(after)
                    except  json.decoder.JSONDecodeError as  e:
                        continue
                    except  BaseException as  e:
                        print(type(e),":",e,":",self.url,":",sparql)
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(type(e),exc_type, fname, exc_tb.tb_lineno)
                    except:
                        pass    
                await asyncio.sleep(10)
        return []