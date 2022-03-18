
from aiohttp.abc import AbstractResolver
import motor.motor_asyncio
import asyncio
import socket
import time
import aiodns
class AsyncResolver2(AbstractResolver):
    def __init__(self, *args, **kwargs) -> None:
        self._loop = asyncio.get_running_loop()
        myclient = motor.motor_asyncio.AsyncIOMotorClient()
        self.resolver = aiodns.DNSResolver(*args, loop=self._loop, **kwargs)
        scrap = myclient.scrap
        self.dns_db = scrap.dns
    async def resolve(self, host: str, port: int = 0, family: int = socket.AF_INET):
        hosts = []
        scrap = {
            "host":host,
            "family":family,
        }
        ans = await self.dns_db.find_one(scrap)
        if ans is not None:
            if ans["daedtime"] > int(time.time()):
                await self.dns_db.delete_many(scrap)
            else:
                return ans["hosts"]
        resp = await self.resolver.gethostbyname(host, family)
        for address in resp.addresses:
             hosts.append({
                "hostname": host,
                "host": address,
                "port": port,
                "family": family,
                "proto": 0,
                "flags": socket.AI_NUMERICHOST | socket.AI_NUMERICSERV,
            })
        await self.dns_db.insert_one({
            "host":host,
            "family":family,
            "hosts":hosts,
            "daedtime":(86400*7*4) + int(time.time()),
        })
        print(hosts)
        return hosts
    async def close(self) -> None:
        self._resolver.cancel()