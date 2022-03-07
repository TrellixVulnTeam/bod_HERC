import asyncio
from traceback import print_tb
from urllib.parse import urlparse
import aiohttp
from uitls.AsyncRobot import Robot
lock_url = []
lock = asyncio.Lock()

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
    
async def async_check_if_website_exists(url_from):
    # await add_url(url_from)
    robot = Robot(url_from)
    # if not await robot.can_fetch(url_from,"*"):
        # print("cant fetch")
        # return False, url_from, None, None ,""
    # wait = await robot.crawl_delay("*")
    # if wait is not None and wait > 0:
    #         print("crawl_delay")
    #         await asyncio.sleep(wait)
    for i in range(20):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url_from,ssl=False) as resp:
                    if resp.ok:
                        mine = resp.headers.get('content-type')
                        text = await  resp.text()
                        # remove_url(url_from)
                        print("good")
                        return True, resp.url, text, mine  ,""
                    
                    if resp.status== 404:
                        break
                    elif resp.status == 403:
                        break
                    else:
                        print( resp.status)
                        pass
        except aiohttp.ClientConnectorError as e:
            print(e)
            break
        except aiohttp.ClientResponseError as e:
            print(e)
            break
        except UnicodeDecodeError as e:
            print(e)
            break
        except aiohttp.ClientOSError as e:
            print(e)
            break
        except aiohttp.ServerDisconnectedError as e:
            print(e)
            continue
    # await remove_url(url_from)
    print("bad")
    return False, url_from, None, None ,""


async def aio_check_if_page_exists(url_from):
    # await add_url(url_from)
    robot = Robot(url_from)
    if not await robot.can_fetch(url_from,"*"):
        return False, url_from, None, None  ,""
    wait = await robot.crawl_delay("*")
    if wait is not None and wait > 0:
            await asyncio.sleep(wait)
    for i in range(20):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url_from,ssl=False) as resp:
                    if resp.ok:
                        mine = resp.headers.get('content-type')
                        text = await  resp.text()
                        print("good")
                        # remove_url(url_from)
                        return True, resp.url, text, mine   ,""
                    if resp.status:
                        pass
        except aiohttp.ClientConnectorError as e:
            print(e)
            break
        except aiohttp.ClientResponseError as e:
            print(e)
            break
        except UnicodeDecodeError as e:
            print(e)
            break
        except aiohttp.ClientOSError as e:
            print(e)
            break
        except aiohttp.ServerDisconnectedError as e:
            print(e)
            break
    # await remove_url(url_from)
    return False, url_from, None, None  ,""