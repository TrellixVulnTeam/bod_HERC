
import asyncio
import aiohttp
import time
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
        # print(self.url)
        async with sem_SPRQL:
            for i in range(i):
                a = []
                try:
                    async with aiohttp.ClientSession() as session:
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
                                print(await r.text())
                                print( r.headers)
                                for header in  r.headers:
                                    if "Retry-After" == header[0]:
                                        try:
                                            after = int(header[1])
                                        except:
                                            after = 10
                                        break
                                else:
                                    after = 10
                                time.sleep(after)
                except KeyboardInterrupt as k:
                    exit()
                except:
                    pass
            return []