import asyncio
async def wait_task(ts):
    cs =[]
    for i in ts:
        cs.append(asyncio.create_task(i))
    return await asyncio.wait(cs)
        