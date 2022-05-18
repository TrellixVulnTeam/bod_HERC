import sys
import aiohttp
import asyncio
import aiofiles
import ijson
import os

from regex import E

endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"


async def SPRQL_GEN(sparql, file_name, online=True, dodgy=False):
    for i in range(5):
        try:
            if online:
                for c in range(2):
                    try:
                        async with aiohttp.ClientSession(headers={"Accept": "application/json"}) as session:
                            async with session.post(endpoint, data={'format': 'json', 'query': sparql}) as r:
                                async with aiofiles.open(file_name, mode='wb') as f:
                                    data = await r.read()
                                    if r.ok:
                                        await f.write(data)
                                        break
                                    elif r.status == 503:
                                        await asyncio.sleep(10*60)
                                        continue
                                    else:
                                        await asyncio.sleep(10)
                    except:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(
                            exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, fname, exc_tb.tb_lineno)
                        print(exc_obj)
                        print("download fails with except will retry")
                        await asyncio.sleep(10)

            size = 0
            if not dodgy or i <= 4:
                try:
                    async with aiofiles.open(file_name, mode='rb') as fs:
                        a = ijson.items(fs, 'results.bindings.item')
                        async for o in a:
                            size = size + 1
                    async with aiofiles.open(file_name, mode='rb') as fs:
                        a = ijson.items(fs, 'results.bindings.item')
                        async for o in a:
                            yield o, size
                        break
                except:
                    continue
            else:
                try:
                    async with aiofiles.open(file_name, mode='rb') as fs:
                        a = ijson.items(fs, 'results.bindings.item')
                        async for o in a:
                            size = size + 1
                            yield o, size
                        break
                except:
                    pass
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(
                exc_tb.tb_frame.f_code.co_filename)[1]
            print(type(exc_obj), exc_type, fname, exc_tb.tb_lineno)
            continue
    size = 0
