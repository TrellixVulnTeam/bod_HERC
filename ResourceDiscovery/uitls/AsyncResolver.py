import asyncio
import socket
import time
from traceback import print_tb
from typing import Any, Dict, List, Type, Union
import aiodns
from aiohttp.abc import AbstractResolver

from ResourceDiscovery.uitls.db import motor_c


class AsyncResolver_DB(AbstractResolver):
    """Use the `aiodns` package to make asynchronous DNS lookups"""

    def __init__(self,db=None,*args: Any, **kwargs: Any) -> None:
        if aiodns is None:
            raise RuntimeError("Resolver requires aiodns library")

        self._loop = asyncio.get_running_loop()
        self._resolver = aiodns.DNSResolver(*args, loop=self._loop, **kwargs)
        self.db = db

    async def resolve(self, host: str, port: int = 0, family: int = socket.AF_INET) -> List[Dict[str, Any]]:
        ## Try DB
        dns = await self.db.get_dns()
        data = await dns.find_one({
            "host":host,
            "family":family
        }) 
        print("DB DNS",data)
        if data is not None:
            if data["datetime"] < time.time() + 24*60*60:
                for i in data["hosts"]:
                    yield i
            else:
                await dns.delete_one({
                    "host":host,
                    "family":family
                }) 
        ## get form DNS
        try:
            resp = await self._resolver.gethostbyname(host, family)
        except aiodns.error.DNSError as exc:
            msg = exc.args[1] if len(exc.args) >= 1 else "DNS lookup failed"
            raise OSError(msg) from exc
        hosts = []
        for address in resp.addresses:
            
               yield {
                    "hostname": host,
                    "host": address,
                    "port": port,
                    "family": family,
                    "proto": 0,
                    "flags": socket.AI_NUMERICHOST | socket.AI_NUMERICSERV,
                }

        if not hosts:
            raise OSError("DNS lookup failed")
         
        if data is None:
            await dns.insert_one({
                "datetime": time.time(),
                "host":host,
                "family":family,
                "hosts":hosts})

    async def close(self) -> None:
        self._resolver.cancel()
