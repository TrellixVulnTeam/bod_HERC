import datetime
from pickle import FALSE
import urllib.robotparser
import asyncio
import motor.motor_asyncio
from urllib.parse import urljoin, urlparse
import time
import aiohttp
from email.utils import parsedate_to_datetime
client = motor.motor_asyncio.AsyncIOMotorClient()


class Robot(urllib.robotparser.RobotFileParser):
    def __init__(self, url ="") -> None:
        super().__init__(url)
        self.daedTime = 0

    async def _read(self) -> None:
        has = False
        text = ""
        self.modified()
        for i in range(20):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.url) as resp:
                        expires = resp.headers.get('expires')
                        if expires is not None:
                            deadtime = parsedate_to_datetime(expires)
                            self.deadtime = deadtime.timestamp()
                        else:
                            self.deadtime = 86400 + time.time()
                        if resp.status in (401, 403):
                            self.disallow_all = True
                            has = True
                        elif resp.status >= 400 and resp.status < 500:
                            self.allow_all = True
                            has = True
                        else:
                            text = await resp.text()
                            self.parse(text)
                            has = True
            except aiohttp.ClientConnectorError as e:
                self.disallow_all = True
                self.deadtime = 86400 + time.time()
                break
            except:
                pass
                
        url_o = urlparse(self.url)
        domain = url_o.scheme + "://"+url_o.netloc
        robots = client['scrape']["robots"]
        document = {
            'disallow_all': self.disallow_all,
            'allow_all': self.allow_all,
            'url': self.url,
            'text': text,
            'deadtime': self.deadtime,
            'last_checked': self.last_checked,
            "domain": domain
        }
        robots.insert_one(document)
        return has

    async def read_db(self) -> None:
        url_o = urlparse(self.url)
        domain = url_o.scheme + "://"+url_o.netloc
        robots = client['scrape']["robots"]
        db_robots = await robots.find_one({"domain": domain})
        if db_robots is not None:
            self.url = db_robots["url"]
            text = db_robots["text"]
            self.parse(text)
            self.disallow_all = db_robots["disallow_all"]
            self.allow_all = db_robots["allow_all"]
            self.url = db_robots["url"]
            self.deadtime = db_robots["deadtime"]
            self.last_checked = db_robots["last_checked"]
        else:
            await self._read()

    async def can_fetch(self, useragent, url) -> None:
        if self.daedTime < time.time():
            await self._read()
        super().can_fetch(useragent, url)

    async def crawl_delay(self, useragent) -> None:
        if self.daedTime < time.time():
            await self._read()
        
        super().crawl_delay(useragent)

    async def request_rate(self, useragent) -> None:
        if self.daedTime < time.time():
            await self._read()
        
        super().request_rate(useragent)

    async def site_maps(self) -> None:
        if self.daedTime < time.time():
            await self._read()
        super().site_maps()



async def test():
    ro = Robot("https://en.wikipedia.org/robots.txt")
    await ro.read_db()
if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
