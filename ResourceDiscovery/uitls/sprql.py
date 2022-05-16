import sys
import aiohttp
import asyncio
import aiofiles
import ijson
import os

endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"


async def SPRQL_GEN(sparql, file_name, endpoint=endpoint, online=True):
    for i in range(10):
        try:
            while online:
                try:
                    async with aiohttp.ClientSession(headers={"Accept": "application/json"}) as session:
                        async with session.request('POST', endpoint, data={'format': 'json', 'query': sparql}) as r:
                            async with aiofiles.open(file_name, mode='wb') as f:
                                if r.ok:
                                    data = await r.read()
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
                    print("download fails with except will retry")
            size = 0
            async with aiofiles.open(file_name, mode='rb') as fs:
                a = ijson.items(fs, 'results.bindings.item')
                async for o in a:
                    size = size + 1
            async with aiofiles.open(file_name, mode='rb') as fs:
                a = ijson.items(fs, 'results.bindings.item')
                async for o in a:
                    yield o, size
                # os.remove(file_name)
                break
        except:
            continue
