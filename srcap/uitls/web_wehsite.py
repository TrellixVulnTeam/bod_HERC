import asyncio
import os
from re import T
import sys
import time
import tldextract
from rfc3986 import urlparse
import validators
from uitls.AsyncRobot import Robot, add_robots, remove_robots
from uitls.asyncio_c import wait_task
from uitls.feedCheck import feedCheck
from uitls.get import aio_check_2, aio_check_if_page_exists, async_check_if_website_exists
from uitls.scan_f import scanHTML
from uitls.webLmmit import qarry_lmmit
from scrape_service.wikidata import wikidata_linked, get_q, sprql_wikidata
import motor.motor_asyncio
from datetime import datetime
from uitls.webLmmit import sem_web
myClient = motor.motor_asyncio.AsyncIOMotorClient()

scrap = myClient.scrap
websiteDb = scrap.website
feedTypes_ends = [
    'feed+json',
    'rss+xml',
    'rss',
    'atom+xml',
    'atom',
    "json"
]


async def remove_website_where(url_from):
    myquery = {
        "url_from": url_from
    }
    if await websiteDb.find_one(myquery) is not None:
        test = await websiteDb.remove(myquery)


async def remove_page_where(url_from, path):
    myquery = {
        "url_from": url_from,
        "points.path": path
    }
    data_website_pull = {'$pull': {"points": {
        "path": path,
    }}}
    if await websiteDb.find_one(myquery) is not None:
        await websiteDb.update_one(myquery, data_website_pull)


async def check_if_needed(url_from, where, type_="website", item=None):
    myquery1 = {
        "url_from": url_from,
        "points": {"$elemMatch": {
            "where": where,
            "type": type_,
        }
        }
    }
    if item is not None:
        myquery1["points"]["$elemMatch"]["ID"] = item
    c = await websiteDb.find_one(myquery1)
    if c is None:
        return True
    return False


async def add_website_where(url_to, where, path, type_="website", item=None, mps={}, d=True, session=None):
    myquery1 = {
        "to_url": url_to,
        "points": {"$elemMatch": {
            "where": where,
            "path": path,
            "type": type_,
        }
        }
    }
    myquery2 = {
        "to_url": url_to,
        "points": {"$elemMatch": {
            "where": where,
            "path": path,
            "type": type_,
        }
        }
    }
    myquery3 = {
        "to_url": url_to,
    }

    data_website_pull = {'$pull': {"points": {
        "where": where,
        "path": path,
        "type": type_
    }}}
    data_website = {'$push': {"points":  {
        "where": where,
        "path": path,
        "type": type_,
        "deadtime": int(time.time()) + (86400*7*4)
    }}}
    a = []
    if item is not None:
        myquery1["points"]["$elemMatch"]["ID"] = item
        myquery2["points"]["$elemMatch"]["ID"] = item
        data_website["$push"]["points"]["ID"] = item
        data_website_pull["$pull"]["points"]["ID"] = item
    # if where == "wikidata":
    #     try:
    #         data, dos = await wikidata_linked(item, mps,session)
    #         if d:
    #             for do in dos:
    #                 a.append(url_add(do, where, item, item_type="website",d=False,session=session))
    #         myquery1["points"]["$elemMatch"]["data"] = data
    #         data_website["$push"]["points"]["data"] = data
    #     except BaseException as e:
    #         pass
    if a != []:
        await wait_task(a)
    c = await websiteDb.find_one(myquery1)
    if c is not None:
        return
    c = await websiteDb.find_one(myquery2)
    if c is not None:
        await websiteDb.update_one(myquery2, data_website_pull)
        await websiteDb.update_one(myquery2, data_website)
    else:
        try:
            await websiteDb.update_one(myquery3, data_website)
        except BaseException as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("ERROR ", type(e), exc_type, fname, exc_tb.tb_lineno)


async def _add_wensite_(url_to, url_from):
    a = urlparse(url_to)
    url_to = a.netloc
    a = urlparse(url_from)
    url_from = a.netloc
    myquery1 = {"to_url": url_to}
    c = await websiteDb.find_one(myquery1)
    if (c) is not None:
        myquery2 = {"url_from": url_from}
        c = await websiteDb.find_one(myquery2)
        if (c) is not None:
            pass
        else:
            data_website = {"$push": {"url_from": url_from}}
            await websiteDb.update_one(myquery2, data_website)
    else:
        data_website = {
            "time": datetime.now(),
            "to_url": url_to,
            "url_from": [url_from],
            "points": [],
        }
        await websiteDb.insert_one(data_website)


async def _add_wensite_(url_to, url_from):
    url_to = str(url_to)
    if (await websiteDb.find_one({"to_url": url_to, "from_url": url_from})) is not None:
        data_website = {
            "$push": {
                "time": datetime.now(),
                "to_url": url_to,
                "from_url": [url_from],
                "date": [],
            }
        }
        myquery = {
            "to_url": url_to
        }
        await websiteDb.insert_one(myquery, data_website)

    elif (await websiteDb.find_one({"url_from": url_from})) is not None:
        myquery = {
            "to_url": url_to
        }
        newvalues = {
            "$push": {
                "url_from": url_from
            }
        }
        await websiteDb.update_one(myquery, newvalues)


async def extract_url(url):
    while True:
        try:
            ext = tldextract.extract(url)
            return ext
        except:
            await asyncio.sleep(0.1)


def urlCheck(url):
    url = url.replace("http://http://", "http://")
    url = url.replace("*", "")
    if url[0] == ":":
        url = url[1:-1]
    try:
        x = urlparse(url)
    except:
        return False, url, None
    if x.scheme != "" and x.netloc != "":
        url_x = x.scheme+"://"+x.netloc
    else:
        url_x = x.netloc
    if x.netloc == "":
        return False, url_x, x
    url = url.replace(" ", "")
    return True, url_x, x


async def add_other_parameter(datas):
    lll = []
    for P in datas:
        async def k(query, data_):
            items = await sprql_wikidata(query)
            for item in items:
                pass
        query = """
        SELECT ?item ?itemLabel ?data WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
          { ?item wdt:"""+P+""" ?data. }
        }
        """
        lll.append(k(query, datas[P]))
    asyncio.gather(*lll)


async def feed_do(data):
    await url_add(data["href"], where="internal", item_type="feed")


async def websub_do(data):
    await url_add(data["href"], where="internal", item_type="feed")


async def just_url_page(url, where, item_type, item=None, Ps={}, session=None, robot=None, text=None, path=None, mine=None):
    try:
        check, _, x = urlCheck(url)
        if not check:
            return False
        check = await check_if_needed(url, where, item_type, item)
        if not check:
            return True
        if text is None:
            async with sem_web:
                check, url_to, text, mine, path, status = await aio_check_if_page_exists(url, robot, session)
            if mine is None:
                mine = ""
            if "css" in mine:
                return False
            if "image" in mine:
                return False
            if "audio" in mine:
                return False
            if "model" in mine:
                return False
            if "video" in mine:
                return False
            if "javascript" in mine:
                return False
            if "ecmascript" in mine:
                return False
            if "font" in mine:
                return False
        else:
            url_to = url
        if not check:
            return False
        check_feed, feeds = await scanHTML(text, url)
        if len(feeds) != 0:
            for feed in feeds:
                try:
                    a_task = asyncio.create_task(just_url_feed(
                        feed["href"], "wikidata", item_type="feed", session=session, robot=robot))
                    await asyncio.wait_for(a_task, timeout=60*40)
                except:
                    pass
        if not check_feed:
            return False
        await add_website_where(url_to, where, path, item_type, item, Ps, d=True, session=session)
        return True
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("ERROR ", (exc_obj), ":", type(exc_obj),
              exc_type, fname, exc_tb.tb_lineno)
        return False


async def just_url_feed(url, where, item_type, item=None, Ps={}, session=None, robot=None, text=None, path=None, mine=None):
    try:
        check = await check_if_needed(url, where, item_type, item)
        if not check:
            return False
        if text is None or path is None:
            async with sem_web:
                check, url_to, text, mine, path, status = await aio_check_if_page_exists(url,  robot, session)
            if mine is None:
                mine = ""
            if "css" in mine:
                return False
            if "image" in mine:
                return False
            if "audio" in mine:
                return False
            if "model" in mine:
                return False
            if "video" in mine:
                return False
            if "javascript" in mine:
                return False
            if "ecmascript" in mine:
                return False
            if "font" in mine:
                return False
        else:
            url_to = url
        if not check:
            return False
        check_feed, datas = feedCheck(text)
        if not check_feed:
            return False
        await add_website_where(url, where, path, item_type, item, Ps, d=True, session=session)
        return True
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("ERROR ", (exc_obj), ":", type(exc_obj),
              exc_type, fname, exc_tb.tb_lineno)
        return False


async def url_add2(url_from, where, item=None, item_type="website",  ps={}, session=None, robot=None):

        try:
            url_from = str(url_from)
            check, _, x = urlCheck(url_from)
            if not check:
                return False
            check = await check_if_needed(url_from, where, item_type, item)
            if not check:
                return True
            async with sem_web:
                if robot is None:
                    robot = await add_robots(url_from, session)
                if robot.disallow_all:
                    return False
                check_website, check_page, url_to, text, mine, path, status = await aio_check_2(url_from, robot, session)
            if mine is None:
                mine = ""
            if not check:
                return False
            if "css" in mine:
                return False
            if "image" in mine:
                return False
            if "audio" in mine:
                return False
            if "model" in mine:
                return False
            if "video" in mine:
                return False
            if "javascript" in mine:
                return False
            if "ecmascript" in mine:
                return False
            if "font" in mine:
                return False
            if check_website:
                await _add_wensite_(url_to, url_from)
            if check_page:
                await just_url_page(url_from, where, item_type, item=item, Ps=ps, session=session, robot=robot, text=text, path=path, mine=mine)
                await just_url_feed(url_from, where, item_type, item=item, Ps=ps, session=session, robot=robot, text=text, path=path, mine=mine)

        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("ERROR ", (exc_obj), ":", type(exc_obj),
                  exc_type, fname, exc_tb.tb_lineno)
            return False
        return True
        # await wait_task(call_async)


async def url_add(url_from, where, item=None, item_type="website", index=0, dectect_item_type=True, Ps={}, d=True, p=False, session=None, robot=None):
    async with qarry_lmmit:
        try:
            url_from = str(url_from)
            check, _, x = urlCheck(url_from)
            if not check:
                return False
            check = await check_if_needed(url_from, where, item_type, item)
            if not check:
                return True
            if robot is None:
                robot = await add_robots(url_from, session)
            url_parts = urlparse(url_from)
            check, url_to, text, mine, path, status = await async_check_if_website_exists(url_from, robot, session)
            if (not check) or (text is None):
                check, url_to, text, mine, path, status = await aio_check_if_page_exists(url_from, robot, session)
                if (not check) or (text is None):
                    await remove_robots(url_from)
                    return False

            if (url_parts.path != "/" and url_parts.path != "") or item_type != "website":
                check_, url_to_, text_, mine_, path_, status_ = await aio_check_if_page_exists(url_from, robot, session)

                if 0 != index:
                    check = check_
                    url_to = url_to_
                    text = text_
                    mine = mine_
                    path = path_
                    status = status_
                if not check_:
                    return False
                if 0 != index and ((not check_ and p) or ((text is None) and p)):
                    await remove_robots(url_from)
                    return False
                if not check_ or ((text is not None)):
                    item = None
                elif 0 < index:
                    check = check_
                    url_to = url_to_
                    text = text_
                    mine = mine_
                    path = path_
                    status = status_
                else:
                    check = check_
                    url_to = url_to_
                    text = text_
                    mine = mine_
                    path = path_
                    status = status_
                if check_ and dectect_item_type:
                    item_type = "page"
            if "css" in mine:
                return False
            if "image" in mine:
                return False
            if "audio" in mine:
                return False
            if "model" in mine:
                return False
            if "video" in mine:
                return False
            if "javascript" in mine:
                return False
            if "ecmascript" in mine:
                return False
            if "font" in mine:
                return False
            if (mine == " ") and (mine is None) or "html" in mine:
                check_html, feeds = await scanHTML(text, url_from)
                if check_html and item_type != "feed":
                    if len(feeds) != 0:
                        for feed in feeds:
                            try:
                                a_task = asyncio.create_task(just_url_feed(
                                    feed["href"], "wikidata", item_type="feed", session=session, robot=robot))
                                await asyncio.wait_for(a_task, timeout=60*40)
                            except:
                                exc_type, exc_obj, exc_tb = sys.exc_info()
                                fname = os.path.split(
                                    exc_tb.tb_frame.f_code.co_filename)[1]
                                print("ERROR ", (exc_obj), ":", type(
                                    exc_obj), " : ", feed, ":", exc_type, fname, exc_tb.tb_lineno)
            else:
                check_html = False
            if (mine == " ") and (mine is None) or ("xml" in mine) or ("rss" in mine) or ("atom" in mine) or ("json" in mine) or item_type == "feed":
                check_feed, datas = feedCheck(text)
                if not check_feed and item_type == "feed":
                    return False
                if check_feed:
                    if check_feed and dectect_item_type:
                        item_type = "feed"
            else:
                check_feed = False
            if not check_html and not check_feed:
                return False
            await _add_wensite_(url_to, url_from)
            await add_website_where(url_to, where, path, item_type, item, Ps, d=True, session=session)
            # await wait_task(call_async)
            return True
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("ERROR ", (exc_obj), ":", type(exc_obj),
                  exc_type, fname, exc_tb.tb_lineno)
            raise exc_obj


def url_sprql(self, url, item):
    while True:
        try:
            ext = tldextract.extract(url)
            break
        except:
            pass
    toplevelHost = ext.domain + "." + ext.suffix
    if toplevelHost in self.registered_domains:
        self.registered_domains[toplevelHost].url_sprql_add(item)
