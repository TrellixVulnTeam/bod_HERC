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

headers = {
    "User-Agent": ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) FeedScaner"),
    "Accept": ("text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"),
    "Accept-Language": ("en-GB,en-US;q=0.9,en;q=0.8"),
    "Connection": ("keep-alive"),
    "Upgrade-Insecure-Requests": ("1"),
    "Sec-Fetch-Dest": ("document"),
    "Sec-Fetch-Mode": ("navigate"),
    "Sec-Fetch-Site": ("cross-site"),
    "Sec-Fetch-User": ("?1"),
    "Pragma": ("no-cache"),
    "Cache-Control": ("no-cache"),
    "TE": ("trailers"),
    "content-length": ("0")
}
lll = {}
class Robot_check():
    def __init__(self, url):
        self. url =  url
        self.robot =Robot(url)
        lll[url] = self.robot
        self.count = 0
    def __enter__(self):
        self.count = self.count+ 1
        with self.robot:
            return self.robot
    def __exit__(self, type, value, traceback):
        self.count = self.count - 1
        self.cr.restore()

class Robot(urllib.robotparser.RobotFileParser):
    def __init__(self, url ="") -> None:
        super().__init__(url)
        self.daedTime = 0
        self.lock_  = asyncio.Lock()


    async def _read(self) -> None:
        has = False
        text = ""
        self.modified()
        for i in range(20):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.url,ssl=False,headers=headers) as resp:
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
                self.deadtime = 86400 + time.time()
                break
            except asyncio.TimeoutError:
                continue
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
        a = super().can_fetch(useragent, url)
        return  a

    async def crawl_delay(self, useragent) -> None:
        if self.daedTime < time.time():
            await self._read()
        
        return super().crawl_delay(useragent)

    async def request_rate(self, useragent) -> None:
        if self.daedTime < time.time():
            await self._read()
        
        return super().request_rate(useragent)

    async def site_maps(self) -> None:
        if self.daedTime < time.time():
            await self._read()
        return super().site_maps()



async def test():
    ro = Robot("https://en.wikipedia.org/robots.txt")
    await ro.read_db()
if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
