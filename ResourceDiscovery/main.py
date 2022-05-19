from ResourceDiscovery.alt_savices.common_crawl import get_some_CC
from srcap.scrape_service.wikidata import Wikidata_qurry_property3
from srcap.uitls.prgoress import get_the_manager
from ResourceDiscovery.uitls.wikidata_qarry import SPARQL_all_website, SPARQL_all_feeds, SPARQL_offical_blog, SPARQL_all_ddd, SPARQL_all_fff, SPARQL_all_cccc
from ResourceDiscovery.uitls.wikidata import wikidata_linked, get_q
from ResourceDiscovery.uitls.test_page import test_page
from ResourceDiscovery.uitls.sprql import SPRQL_GEN
from ResourceDiscovery.uitls.scan_f import scanHTML
from ResourceDiscovery.uitls.robot import Robots
from ResourceDiscovery.uitls.feedCheck import feedCheck
from ResourceDiscovery.uitls.db import get_wikidataDb
import asyncio
import os
import socket
import sys
import time
from urllib.parse import urljoin, urlparse
from urllib import robotparser
from alive_progress import alive_bar

import aiohttp
import enlighten
from progress.bar import Bar


debug = False


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


async def check_resource(url, type_, where):
    wikidataDb = await get_wikidataDb()
    a = urlparse(url)
    query3 = {
        "to_url":  a.scheme+"://"+a.netloc,
        "points": {"$elemMatch": {
            "where": where,
            "path": a.path,
            "type": type_,
            "datetime": {"$lte":  time.time() - 2592000}
        }
        }
    }
    return await wikidataDb.count_documents(query3) != 0


async def resource_add(url, data=None, item=None, value=None, prop=None, type_="unknown", where="wikidata"):

    a = urlparse(url)
    doc_to_url = {
        "to_url":  a.scheme+"://"+a.netloc,
    }
    query3 = {
        "to_url":  a.scheme+"://"+a.netloc,
        "points": {"$elemMatch": {
            "where": where,
            "path": a.path,
            "type": type_,
            "data":  data
        }
        }
    }
    wikidataDb = await get_wikidataDb()
    # ax = await wikidata_linked(Q, magic=[], session=session)
    if await wikidataDb.count_documents(doc_to_url) == 0:
        # ADD DOC
        c = {
            "to_url":  a.scheme+"://"+a.netloc,
            "datetime": time.time(),
            "points": [{
                "where": where,
                "path": a.path,
                "type": type_,
                "datetime": time.time(),
            }]
        }
        if prop is not None:
            c["points"][0]["prop"] = prop
        if value is not None:
            c["points"][0]["value"] = value
        if item is not None:
            c["points"][0]["item"] = item
        if data is not None:
            c["points"][0]["data"] = data
        await wikidataDb.insert_one(c)
    elif await wikidataDb.count_documents(query3) != 0:
        # update
        c = {
            "$set": {"datetime": time.time(),
                     "points.$.data": data,
                     "points.$.datetime": time.time()
                     }
        }
        if prop is not None:
            c["$set"]["points.$.prop"] = prop
        if value is not None:
            c["$set"]["points.$.value"] = value
        if item is not None:
            c["$set"]["points.$.item"] = item
        if data is not None:
            c["$set"]["points.$.data"] = data
        # await wikidataDb.update_one(query3, c)
    else:
        # ADD DATA BIT
        c = {
            "$set": {
                "datetime": time.time(),
            },
            "$push": {"points": {
                "where": where,
                "path": a.path,
                "type": type_,
                "datetime": time.time(),
                "data": data
            }}
        }
        if prop is None:
            c["$push"]["points"]["prop"] = prop
        if value is None:
            c["$push"]["points"]["value"] = value
        if item is None:
            c["$push"]["points"]["item"] = item
        if data is not None:
            c["$push"]["points"]["data"] = data
        await wikidataDb.update_one(doc_to_url, c)

sprql_endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"


async def get_ting(url, prop=None, item=None, sem=None, data=None, type_="unknown", where="wikidata", value=None, session=None):
    if await check_resource(url, type_, where):
        return
    try:
        async with sem:
            rb = Robots(urljoin(url, '/robots.txt'))
            await rb.read(session)
            if rb.disallow_all:
                return False
            a = await test_page(url, session, rb, sem=sem)
            check_website, check_webpage, html, status, mime = a
            if not check_website or not check_webpage:
                return False
            if item == None:
                Q = get_q(item)
                data = await wikidata_linked(Q, session=session)
            else:
                Q = None
            await resource_add(url, item=Q, type_=type_, data=data, prop=prop, value=value, type_=type_, where=where)
        if type_ != "feed":
            isGood, feeds = await scanHTML(html, url)
            async with sem:
                for feed in feeds:
                    try:
                        check_website, check_webpage, html, status, mime = await test_page(feed, session, rb, sem=sem)
                        check, urls = feedCheck(html)
                        if check:
                            await resource_add(feed, type_="feed")
                    except:
                        pass
        else:
            try:
                check_website, check_webpage, html, status, mime = await test_page(feed, session, rb, sem=sem)
                await resource_add(feed, type_="feed")
            except:
                pass
    except:
        pass


async def do_thing(datas, bar_done, name="", name_item_id=None, name_prop_url=None, where="wikidata", prop="", sem=None, type_=None, value_name=None):
    pending2 = []
    # timeout = aiohttp.ClientTimeout(total=90)
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(70), connector=aiohttp.TCPConnector(family=socket.AF_INET,   verify_ssl=False)) as session:
            for data in datas:
                try:
                    # Get item
                    if name_item_id is not None:
                        item = data[name_item_id]["value"]
                    else:
                        if "item" not in data.keys():
                            continue
                        item = data["item"]["value"]
                    # Get URL
                    if name_prop_url is not None:
                        url = data[name_prop_url]["value"]
                    else:
                        url = data[name]["value"]
                    # Get Value
                    if value_name is not None:
                        value = data[value_name]["value"]
                    else:
                        value = None

                    pending2.append(asyncio.create_task(get_ting(
                        url, prop=prop, item=item, type_=type_, sem=sem, value=value, where=where, session=session)))
                except:
                    pass
                bar_done.update()
                if len(pending2) > 350:
                    await asyncio.wait(pending2)
                    pending2 = []
        if len(pending2) != 0:
            await asyncio.wait(pending2)
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(
            exc_tb.tb_frame.f_code.co_filename)[1]
        print(type(exc_obj), exc_type, fname, exc_tb.tb_lineno)


def check():
    pass


async def get_wikidata(name, prop, quarry, lock_SPRQL, type_="unknown", value_name=None, dodgy=True):
    sem = asyncio.Semaphore(50)
    things = []
    count = 0
    pending = []
    manager = get_the_manager()
    bar_done = manager.counter(total=1, desc='bar_done: '+name, unit='ticks')
    bar_start = manager.counter(total=1, desc='bar_start: '+name, unit='ticks')
    while True:
        try:
            async for data_i, size in SPRQL_GEN(quarry,  name+".json", dodgy=dodgy):
                bar_done.total = size
                bar_start.total = size
                count = size
                things.append(data_i)
                bar_start.update()
                if len(things) > 100:
                    await do_thing(things, bar_done, name=name, sem=sem, prop=prop, type_=type_, value_name=value_name)
                    things = []
                if count == 0:
                    continue
        except:
            continue
        return True


async def main_inyourarea(lock_SPRQL):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(70), connector=aiohttp.TCPConnector(family=socket.AF_INET,   verify_ssl=False)) as session:
        url = "https://www.inyourarea.co.uk/"
        pass


async def main_mediabiasfactcheck(lock_SPRQL):
    pass


async def main_allsides(lock_SPRQL):
    pass


async def main_news(lock_SPRQL):
    pass


async def main_ResourceDiscovery_Q_gen(lock_SPRQL):
    async for data_i, size in SPRQL_GEN(SPARQL_all_ddd,  "SPARQL_all_ddd.json"):
        Q = get_q(data_i["type_of_Wikidata_property"]["value"])
        text_ddd = SPARQL_all_fff % (Q)
        async for data_i_x2, size in SPRQL_GEN(text_ddd,  "SPARQL_all_fff.json"):
            P = get_q(data_i_x2["type_of_Wikidata_property"]["value"])
            text_ccc = SPARQL_all_cccc % (P)
            formatter_URL = data_i_x2["formatter_URL"]["value"]
            async for data_i_x3, size in SPRQL_GEN(text_ccc,  "SPARQL_all_cccc.json"):
                while not await get_wikidata(name="item", type_="unknown", prop=P, lock_SPRQL=lock_SPRQL, quarry=text_ccc, dodgy=True):
                    pass
        # formatter URL


async def FFFFF(name):
    async for i in get_some_CC():
        print(i)


async def main_ResourceDiscovery(name):
    lock_SPRQL = asyncio.Lock()
    while True:
        try:
            while not await get_wikidata(name="official_website", type_="website", prop="P856", lock_SPRQL=lock_SPRQL, quarry=SPARQL_all_website):
                pass
        except:
            pass
        try:
            while not await get_wikidata(name="SPARQL_offical_blog", type_="blog", prop="P1581", lock_SPRQL=lock_SPRQL, quarry=SPARQL_offical_blog):
                pass
        except:
            pass
        try:
            while not await get_wikidata(name="SPARQL_all_feeds", type_="feed", prop="P1019", lock_SPRQL=lock_SPRQL, quarry=SPARQL_all_feeds):
                pass
        except:
            pass
        await main_ResourceDiscovery_Q_gen(lock_SPRQL)
        # CC
        # NEWS SCORES UK

# await offical_blog(lock_SPRQL)
# await feeds(lock_SPRQL)
