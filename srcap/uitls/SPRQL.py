
import asyncio
import json
import os
import sys
import aiofiles
import aiohttp
import ijson
import time
sem_SPRQL = asyncio.BoundedSemaphore(300)


async def SPRQL_GEN(sparql, endpoint, file_name, online=True):
    while True:
        try:
            while online:
                try:
                    async with aiohttp.ClientSession(headers={"Accept": "application/json"}) as session:
                        async with session.request('POST', endpoint, data={'format': 'json', 'query': sparql}) as r:
                            async with aiofiles.open(file_name, mode='wb') as f:
                                if r.ok:
                                    print("download ok")
                                    async for data, _ in r.content.iter_chunks():
                                        await f.write(data)
                                    print("download done")
                                    break
                                else:
                                    print("download fails will retry")
                except:
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
                break
        except:
            continue
