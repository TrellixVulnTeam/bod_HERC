
import asyncio
import json
import os
import sys
import aiofiles
import aiohttp
import ijson
import time
sem_SPRQL = asyncio.BoundedSemaphore(300)

lock = asyncio.Lock()


async def SPRQL_GEN(sparql, endpoint, file_name, online=True):
    for i in range(10):
        try:
            while online:
                try:
                    async with lock:
                        async with aiohttp.ClientSession(headers={"Accept": "application/json"}) as session:
                            async with session.request('POST', endpoint, data={'format': 'json', 'query': sparql}) as r:
                                async with aiofiles.open(file_name, mode='wb') as f:
                                    if r.ok:
                                        async for data, _ in r.content.iter_chunks():
                                            await f.write(data)
                                        break
                                    elif r.status == 503:
                                        await asyncio.sleep(10*60)
                                        continue
                                    else:
                                        print("test:", r.status)
                                        print("download fails will retry")
                                        await asyncio.sleep(10)
                except BaseException as e:
                    print("download fails with except will retry")
                    print(e)
            size = 0
            async with aiofiles.open(file_name, mode='rb') as fs:
                a = ijson.items(fs, 'results.bindings.item')
                async for o in a:
                    size = size + 1
            async with aiofiles.open(file_name, mode='rb') as fs:
                a = ijson.items(fs, 'results.bindings.item')
                async for o in a:
                    yield o, size
                os.remove(file_name)
                break
        except:
            continue
