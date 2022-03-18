
import asyncio


sem_web = asyncio.BoundedSemaphore(400)