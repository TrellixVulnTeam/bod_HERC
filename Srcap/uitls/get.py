from uitls.webLmmit import sem_web
import asyncio
import os
import sys
from tkinter.messagebox import NO
from traceback import print_tb
from urllib.parse import urljoin, urlparse
import aiohttp
from uitls.AsyncRobot import Robot
lock_url = []
lock = asyncio.BoundedSemaphore(300)
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


async def async_check_if_website_exists(url_from, robot, session):
    for i in range(10):
        async with sem_web:
            if robot is not None:
                try:
                    try:
                        fetch = await robot.can_fetch("FeedScaner", url_from, session)
                        if not fetch:
                            return False, url_from, None, None, "", None
                    except:
                        pass
                    
                    try:
                        time_ = await robot.crawl_delay("FeedScaner", session)
                    except:
                        time_ = 0
                    if time_ is not None:
                        await asyncio.sleep(int(time_))
                except BaseException as e:
                    print((e), ":", type(e), ":", url_from)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(
                        exc_tb.tb_frame.f_code.co_filename)[1]
                    print(type(e), exc_type, fname, exc_tb.tb_lineno)
            try:
                async with session.get(url_from, ssl=False, headers=headers) as resp:
                    o = urlparse(str(resp.url))
                    try:
                        mine = resp.headers.get('content-type')
                    except:
                        mime = ""
                    try:
                        try:
                            text = await resp.text()
                        except:
                            text = await resp.text('ISO-8859-1')
                    except:
                        text = ""
                    return True, str(resp.url), text, mine, o.path, resp.status
            except aiohttp.ClientConnectorError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
                break
            except aiohttp.ClientResponseError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
                continue
            except UnicodeDecodeError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
                break
            except aiohttp.ClientOSError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
                continue
            except aiohttp.ServerDisconnectedError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
                continue
            except asyncio.TimeoutError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
                continue
            except asyncio.exceptions.TimeoutError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
                continue
            except asyncio.TimeoutError:
                    break
            except BaseException as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
        # await remove_url(url_from)
    return False, url_from, None, None, "", None


async def aio_check_if_page_exists(url_from, robot, session):
    for i in range(10):
        async with sem_web:
            try:
                if robot is not None:
                    try:
                        fetch = await robot.can_fetch("FeedScaner", url_from, session)
                        if not fetch:
                            return False, url_from, None, None, "", None
                    except:
                        pass
                    
                    try:
                        time = await robot.crawl_delay("FeedScaner", session)
                    except:
                        time = 0
                    if (time is not None) and time != 0:
                        print("time:", time)
                        await asyncio.sleep(int(time))
            except BaseException as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
            try:
                async with session.get(url_from, ssl=False, headers=headers) as resp:
                    o = urlparse(str(resp.url))
                    mine = resp.headers.get('content-type')
                    try:
                            text = await resp.text()
                    except:
                            text = await resp.text('ISO-8859-1')
                    if resp.ok:
                        # ok the page is reak
                        return True, str(resp.url), text, mine, o.path, resp.status
                    if resp.status == 404:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    if resp.status == 201:
                        text = await resp.text()
                        return True, url_from, text, mine,  o.path, resp.status
                    if resp.status == 202:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    if resp.status == 203:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 404:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 500:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 501:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 502:
                        continue
                    elif resp.status == 503:
                        continue
                    elif resp.status == 504:
                        continue
                    elif resp.status == 505:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 404:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 506:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 507:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 508:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 510:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 511:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    elif resp.status == 508:
                        text = await resp.text()
                        return False, url_from, text, mine, o.path, resp.status
                    else:
                        return False, url_from, text, mine, o.path, resp.status
            except aiohttp.ClientConnectorError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                break
            except aiohttp.ClientResponseError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                break
            except UnicodeDecodeError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                break
            except RuntimeError as e:
                break
            except asyncio.TimeoutError:
                    break
            except aiohttp.ClientOSError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
                continue
            except aiohttp.ServerDisconnectedError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
                continue
            except asyncio.TimeoutError as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                continue
            except RuntimeError as e:
                break
            except BaseException as e:
                print("ERROR ",(e), ":", type(e), ":", url_from)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(type(e), exc_type, fname, exc_tb.tb_lineno)
        # await remove_url(url_from)
    return False, url_from, None, None, "", None
