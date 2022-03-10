import asyncio
from traceback import print_tb
from urllib.parse import urljoin, urlparse
import aiohttp
from uitls.AsyncRobot import Robot
lock_url = []
lock = asyncio.Lock()
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
async def remove_url(url):
    c= urlparse(url)
    async with lock:
        lock_url.remove(c.scheme+'://'+c.netloc)
async def add_url(url):
    c= urlparse(url)
    async with lock:
        while (c.scheme+'://'+c.netloc) in lock_url:
            await asyncio.sleep(0.01)
        lock_url.append(c.scheme+'://'+c.netloc)


sem_web = asyncio.BoundedSemaphore(60)  
async def async_check_if_website_exists(url_from):
    async with sem_web:
        # await add_url(url_from)
        # robot = Robot(urljoin(url_from,"/robots.txt"))
        # if not await robot.can_fetch(url_from,"*"):
            # print("cant fetch")
            # return False, url_from, None, None ,""
        # wait = await robot.crawl_delay("*")
        # if wait is not None and wait > 0:
                # await asyncio.sleep(wait)
        for i in range(5):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url_from,ssl=False,headers=headers) as resp:
                            mine = resp.headers.get('content-type')
                            text = await  resp.text()
                            return True, str(resp.url), text, mine  ,"" ,resp.status
            except aiohttp.ClientConnectorError as e:
                print("ClientConnectorError:",e,"url:",url_from)
                return False, url_from, None, None ,""
                break
            except aiohttp.ClientResponseError as e:
                print("ClientResponseError:",e,"url:",url_from)
                continue
            except UnicodeDecodeError as e:
                print("UnicodeDecodeError:",e,"url:",url_from)
                break
            except aiohttp.ClientOSError as e:
                print("ClientOSError:",e,"url:",url_from)
                break
            except aiohttp.ServerDisconnectedError as e:
                print("ServerDisconnectedError:",e,"url:",url_from)
                break
            except asyncio.TimeoutError as e:
                continue
        # await remove_url(url_from)
        return False, url_from, None, None ,""


async def aio_check_if_page_exists(url_from):
    async with sem_web:
        # do robots
        # robot = Robot(urljoin(url_from,"/robots.txt"))
        # if not await robot.can_fetch(url_from,"*"):
        #     return False, url_from, None, None  ,""
        # wait = await robot.crawl_delay("*")
        # if wait is not None and wait > 0:
        #         await asyncio.sleep(wait)
        # do reqeset
        for i in range(5):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url_from,ssl=False,headers=headers) as resp:
                        if resp.ok:
                            # ok the page is reak
                            mine = resp.headers.get('content-type')
                            text = await  resp.text()
                            return True, str(resp.url), text, mine   ,"" ,resp.status
                        if resp.status:
                            return False, url_from, None, None  ,""
            except aiohttp.ClientConnectorError as e:
                print("ClientConnectorError:",e,"url:",url_from)
                return False, url_from, None, None ,""
                break
            except aiohttp.ClientResponseError as e:
                print("ClientResponseError:",e,"url:",url_from)
                break
            except UnicodeDecodeError as e:
                print("UnicodeDecodeError:",e,"url:",url_from)
                break
            except aiohttp.ClientOSError as e:
                print("ClientOSError:",e,"url:",url_from)
                break
            except aiohttp.ServerDisconnectedError as e:
                print("ServerDisconnectedError:",e,"url:",url_from)
                break
            except asyncio.TimeoutError as e:
                continue
        # await remove_url(url_from)
        return False, url_from, None, None  ,""