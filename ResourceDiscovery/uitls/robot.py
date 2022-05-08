import asyncio
import os
import sys
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
    async def read(self, session):
        for i in range(5):
            try:
                async with session.get(self.url, ssl=False, headers=headers, max_redirects=30) as response:
                    if response.status in (401, 403):
                        self.disallow_all = True
                        return False
                    elif response.status >= 400 and response.status < 500:
                        self.allow_all = True
                        return True
                    else:
                        try:
                            raw = await response.text()
                        except:
                            raw = await response.text('ISO-8859-1')
                        self.parse(raw)
                    return True
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
