import ctypes
import datetime
import os
from pickle import FALSE
import urllib.robotparser
import asyncio
from charset_normalizer import from_bytes
import motor.motor_asyncio
from urllib.parse import urljoin, urlparse
import time
import aiohttp
try:
    from uitls.webLmmit import sem_web
except:
    sem_web = asyncio.BoundedSemaphore(1000)
from email.utils import parsedate_to_datetime
import sys
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
local_robots = {}
llls = {}
robots = client['scrape']["robots"]


def ref_count(a):
    return ctypes.c_long.from_address(id(a)).value


async def remove_robots(url):
    return
    o = urlparse(url)
    temp_url = o.scheme + "://" + o.netloc
    if (temp_url in local_robots.keys()) and (llls[temp_url] == 0):
        del local_robots[temp_url]
    else:
        llls[temp_url] = llls[temp_url] - 1


async def add_robots(url, session):
    local_robots = Robot(url)
    return local_robots
    temp_url = o.scheme + "://" + o.netloc
    try:
        if temp_url in local_robots.keys():
            llls[temp_url] = llls[temp_url] + 1
        else:
            local_robots[temp_url] = Robot(url)
            llls[temp_url] = 1
            await local_robots[temp_url].read_db(session)
        return local_robots[temp_url]
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print((exc_obj), ":", type(exc_obj), exc_type, fname, exc_tb.tb_lineno)


class Robot(urllib.robotparser.RobotFileParser):
    def __init__(self, url="") -> None:
        url = urljoin(url, "/robots.txt")
        super().__init__(url)
        self.deadtime = 0
        self.lock_ = asyncio.Lock()

    async def _read(self, session) -> None:
        has = False
        text = ""
        self.modified()
        self.disallow_all = False
        self.allow_all = False
        self.deadtime = (86400*7*4) + int(time.time())
        for i in range(4):
                try:
                    async with session.get(self.url, ssl=False, headers=headers) as resp:
                        if resp.status in (401, 403):
                            self.disallow_all = True
                            has = True
                            break
                        elif resp.status in (429, 503):
                            await asyncio.sleep(10)
                        elif resp.status >= 400 and resp.status < 500:
                            self.allow_all = True
                            has = True
                            self.disallow_all = False
                            break
                        else:
                            try:
                                text = await resp.text()
                            except (LookupError, UnicodeDecodeError):
                                try:
                                    text = await resp.text('ISO-8859-1')
                                except (LookupError, UnicodeDecodeError):
                                    text = await resp.content.read()
                                    print(from_bytes(text))
                            self.parse(text)
                            self.disallow_all = False
                            break
                except aiohttp.ClientConnectorError as e:
                    self.disallow_all = True
                    break
                except asyncio.TimeoutError as e:
                    continue
                except UnicodeDecodeError as e:
                    break
                except asyncio.TimeoutError:
                    break

                except RuntimeError as e:
                    break
                except:
                    print("error unkown")
                    continue

        url_o = urlparse(self.url)
        domain = url_o.scheme + "://"+url_o.netloc
        db_robots = await robots.find_one({"domain": domain})
        if db_robots is not None:
            await robots.delete_many({"domain": domain})

        document = {
            'disallow_all': self.disallow_all,
            'allow_all': self.allow_all,
            'url': self.url,
            'text': text,
            'deadtime': self.deadtime,
            'last_checked': self.last_checked,
            "domain": domain
        }

        db_robots = await robots.find_one({"domain": domain})
        if db_robots is not None:
            robots.delete_many(db_robots)
        robots.insert_one(document)
        return has

    async def read_db(self, session) -> None:
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
        if (db_robots is None) or (self.deadtime is None) or (self.deadtime < int(time.time())):
            await self._read(session)

    async def can_fetch(self, useragent, url, session) -> None:
        if (self.deadtime is None):
            await self._read(session)
        elif (self.deadtime is None) or int(self.deadtime) < int(time.time()):
            await self._read(session)
        a = super().can_fetch(useragent, url)
        return a

    async def crawl_delay(self, useragent, session) -> None:
        if (self.deadtime is None):
            await self._read(session)
        elif (self.deadtime is None) or int(self.deadtime) < int(time.time()):
            await self._read(session)

        return super().crawl_delay(useragent)

    async def request_rate(self, useragent, session) -> None:
        if (self.deadtime is None):
            await self._read(session)
        elif (self.deadtime is None) or int(self.deadtime) < int(time.time()):
            await self._read(session)

        return super().request_rate(useragent)

    async def site_maps(self, session) -> None:
        if (self.deadtime is None):
            await self._read(session)
        elif (self.deadtime is None) or int(self.deadtime) < int(time.time()):
            await self._read(session)
        return super().site_maps()


async def test2(url, session):
    ro = await add_robots("https://en.wikipedia.org/", session)
    await ro.read_db(session)
    a = await ro.can_fetch("*", "https://en.wikipedia.org/", session)


async def test():
    c = aiohttp.TCPConnector(enable_cleanup_closed=True)
    async with aiohttp.ClientSession(connector=c) as session:
        ro = await add_robots("https://en.wikipedia.org/", session)
        await ro.read_db(session)
        a = await ro.can_fetch("*", "https://en.wikipedia.org/", session)
        await remove_robots("https://en.wikipedia.org/")
        await test2("https://en.wikipedia.org/", session)
if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
