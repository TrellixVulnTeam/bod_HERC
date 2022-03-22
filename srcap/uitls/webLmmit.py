
import asyncio


sem_web = asyncio.BoundedSemaphore(300)

qarry_lmmit = asyncio.Semaphore(100)