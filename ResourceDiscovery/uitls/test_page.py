

import asyncio
import os
import sys
from urllib import robotparser
from urllib.parse import urljoin
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


async def test_page(url, session, rb, sem=None):
    if not rb.can_fetch("*", url):
        return False, False, "", 000, ""
    time = rb.request_rate("*")
    server_discoonet = 0
    check_wesite = True
    if time is not None:
        await asyncio.sleep(time)
    for i in range(5):
        try:
            async with session.get(url, ssl=False, headers=headers, max_redirects=30) as response:
                try:
                    mime = response.headers['content-type']
                except:
                    mime = ""
                if response.ok:
                    try:
                        text = await response.text()
                    except:
                        text = await response.text('ISO-8859-1')
                    return True, True, text, response.status, mime
                else:
                    try:
                        text = await response.text()
                    except:
                        text = await response.text('ISO-8859-1')
                    return True, False, text, response.status, mime
        except OSError as e:
            print("e", e)
            return check_wesite, False, "", 000, ""
        except asyncio.exceptions.TimeoutError:
            check_wesite = True
            break
        except ValueError as e:
            break
        except aiohttp.ClientPayloadError as e:
            break
        except aiohttp.InvalidURL as e:
            break
        except aiohttp.ClientConnectionError as e:
            break
        except aiohttp.TooManyRedirects as e:
            break
        except aiohttp.ServerDisconnectedError as e:
            if server_discoonet < 2:
                server_discoonet = server_discoonet + 1
                continue
            break
        except BaseException as e:
            if time is not None:
                await asyncio.sleep(time)
            else:
                # need to be polite
                await asyncio.sleep(0.1)
            pass
    return check_wesite, False, "", 000, ""
