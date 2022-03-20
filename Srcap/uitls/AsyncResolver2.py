
from aiohttp.abc import AbstractResolver
import motor.motor_asyncio
import asyncio
import socket
import time
import aiodns
import ipaddress
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
            if ans["daedtime"] > int(time.time()) or len(ans["hosts"])==0:
                await self.dns_db.delete_many(scrap)
            else:
                return ans["hosts"]
        for i in range(10):
            try:
                resp = await self.resolver.gethostbyname(host, family)
            except:
                await asyncio.sleep(1.1)
                continue
            for address in resp.addresses:
                try:
                    ip = ipaddress.ip_address(address)
                    if ip.is_private:
                        continue
                    if not ip.is_global:
                        continue
                    if ip.is_loopback:
                        continue
                    if ip.is_multicast:
                        continue
                    if ip.is_link_local:
                        continue
                    if ip. is_unspecified:
                        continue
                except:
                    continue
                hosts.append({
                    "hostname": host,
                    "host": address,
                    "port": port,
                    "family": family,
                    "proto": 0,
                    "flags": socket.AI_NUMERICHOST | socket.AI_NUMERICSERV,
                })
            if len(hosts) !=0:
                
                await self.dns_db.insert_one({
                "host":host,
                "family":family,
                "hosts":hosts,
                "daedtime":(86400*7*4) + int(time.time()),
                })
                return hosts
            else:
                await asyncio.sleep(1.1)
        return hosts
    async def close(self) -> None:
        self._resolver.cancel()