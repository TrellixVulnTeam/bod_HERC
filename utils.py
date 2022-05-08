
import asyncio
import threading


def asynchronous_thread_task(fun, loop, id=0):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fun(id))
    # loop.run_forever()
