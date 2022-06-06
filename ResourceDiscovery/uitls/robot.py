import asyncio
import os
import sys
import time
from urllib import robotparser

import aiohttp

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


class Robots(robotparser.RobotFileParser):
    async def read(self, session=None,db=None):
        robots =  None
        if db is not None:
            robots = await db.get_robots()
            ccc = {
                "url":self.url
            }
            data = await robots.find_one(ccc) 
            deadline = time.time() + 24*60*60
            if (data is not None) and (data["datetime"] < deadline):
                self.disallow_all = data["disallow_all"]
                self.allow_all = data["allow_all"]
                self.parse(data["text"])
                return self.disallow_all
        for i in range(5):
            try:
                async with session.get(self.url, headers=headers, max_redirects=30) as response:
                    if response.status in (401, 403):
                        self.disallow_all = True
                        check = False
                        raw= ""
                    elif response.status >= 400 and response.status < 500:
                        self.allow_all = True
                        check =  True
                        raw= ""
                    else:
                        try:
                            raw = await response.text()
                            check =True
                        except:
                            raw = await response.text('ISO-8859-1')
                            check =True
                        self.parse(raw)
                    if data is None:
                        if len(raw) <= 512000:
                            await robots.insert_one({"url":self.url,"disallow_all":self.disallow_all,"allow_all":self.allow_all,"datetime": time.time(),"text":raw})
                    else:
                        if len(raw) <= 512000:
                            await robots.update_one(
                                ccc,
                                {
                                    "url":self.url,
                                    "disallow_all":self.disallow_all,
                                    "allow_all":self.allow_all,
                                    "datetime": time.time(),
                                    "text":raw
                                })
                    return check
            except aiohttp.ClientConnectorError as e:
                self.disallow_all = True
                return False
            except OSError as e:
                self.disallow_all = True
                return False
            except aiohttp.InvalidURL as e:
                break
            except ValueError as e:
                break
            except aiohttp.ClientConnectionError as e:
                return False
            except aiohttp.ClientPayloadError as e:
                self.disallow_all = True
                return False
            except aiohttp.ServerDisconnectedError as e:
                self.allow_all = True
                return False
            except asyncio.exceptions.TimeoutError:
                self.allow_all = True
                break
            except aiohttp.TooManyRedirects as e:
                self.allow_all = True
                return True
            except BaseException as e:
                await asyncio.sleep(0.5)
        return False
