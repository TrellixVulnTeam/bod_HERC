from random import random
from anyio import sleep
from numpy import append
from ResourceDiscovery.alt_savices.allsides import get_all_sides
from ResourceDiscovery.alt_savices.common_crawl import get_some_CC
from ResourceDiscovery.alt_savices.url import news_urls, news_left_right
from ResourceDiscovery.uitls.AsyncResolver import AsyncResolver_DB
# from srcap.scrape_service.wikidata import Wikidata_qurry_property3
from srcap.uitls.prgoress import get_the_manager
from ResourceDiscovery.uitls.wikidata_qarry import SPARQL_all_website, SPARQL_all_feeds, SPARQL_offical_blog, SPARQL_all_ddd, SPARQL_all_fff, SPARQL_all_cccc
from ResourceDiscovery.uitls.wikidata import wikidata_linked, get_q
from ResourceDiscovery.uitls.test_page import test_page
from ResourceDiscovery.uitls.sprql import SPRQL_GEN
from ResourceDiscovery.uitls.scan_f import scanHTML
from ResourceDiscovery.uitls.robot import Robots
from ResourceDiscovery.uitls.feedCheck import feedCheck
from ResourceDiscovery.uitls.db import  motor_c
import asyncio
import os
import socket
import sys
import time
import csv
import asyncio
from urllib.parse import urljoin, urlparse
from urllib import robotparser
from alive_progress import alive_bar
import gc
import aiohttp
import enlighten
from progress.bar import Bar
from pympler.tracker import SummaryTracker
from pympler import muppy
from pympler import summary
import random

all_objects = muppy.get_objects()

tracker = SummaryTracker()

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


async def check_resource(url, type_, where,db=None):
    try:
        wikidataDb = await  db.get_ResourceDiscovery()
        a = urlparse(url)
        query3 = {
            "to_url":  a.scheme+"://"+a.netloc,
            "points": {"$elemMatch": {
                "where": where,
                "path": a.path,
                "type": type_,
                "datetime": {"$lte":  time.time() + 2592000}
            }
            }
        }
        a = await wikidataDb.count_documents(query3)
        return a != 0
    except BaseException as e:
        print("error:",e)
        return False


async def resource_add(url, db=None,data=None, item=None, value=None, prop=None, type_="unknown", where="wikidata"):

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
    wikidataDb = await db.get_ResourceDiscovery()
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


async def get_ting(url,lock,db=None, prop=None, item=None, sem=None, data=[], type_="unknown", where="wikidata", value=None, session=None,db_check=True):
    try:
        async with sem:
            if not await check_resource(url, type_, where,db=db):
                    gc.collect()
                    return True
            
            rb = Robots(urljoin(url, '/robots.txt'))
            await rb.read(session,db=db)
            
            if rb.disallow_all:
                gc.collect()
                return False
            
            a = await test_page(url, session, rb)
            check_website, check_webpage, html, status, mime = a
            if not check_website or not check_webpage:
                gc.collect()
                return False
            if type_ != "feed":
                isGood_HTML, feeds = await scanHTML(html, url)
                if not isGood_HTML:
                    gc.collect()
                    return False
            
            if type(item) == list:
                for i in item:
                    Q = get_q(i)
                    data = {** await wikidata_linked(Q,lock,db=db, session=session), **data}
            elif item is not None:
                Q = get_q(item)
                data = (await wikidata_linked(Q,lock,db=db, session=session))+data
            else:
                Q = None
            if type_ != "feed":
                if isGood_HTML:
                    await resource_add(url, data=data,db=db, item=Q, type_=type_, prop=prop, value=value, where=where)
                       
                for feed in feeds:
                    try:
                        check_website, check_webpage, text, status, mime = await test_page(feed, session, rb)
                        if not check_webpage:
                            continue
                        check, urls = feedCheck(text)
                        if check:
                            await resource_add(feed,db=db, type_="feed")
                            
                    except:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        print(exc_type, exc_obj, exc_tb,fname)
            else:
                try:
                    check_website, check_webpage, html, status, mime = await test_page(feed, session, rb)
                    await resource_add(feed, type_="feed")
                except:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, exc_obj, exc_tb,fname)
    except BaseException as e:
        print(e)
        gc.collect()
        return False
    gc.collect()
    return True


async def do_thing(datas, bar_done,lock,db=None, name="", name_item_id=None, name_prop_url=None, where="wikidata", prop="", sem=None, type_=None, value_name=None):
    timeout = aiohttp.ClientTimeout(10)
    loop = asyncio.get_event_loop()
    # resolver = AsyncResolver_DB(db,loop=loop)
    connector = aiohttp.TCPConnector(family=socket.AF_INET, verify_ssl=False)
    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        pending2 = []
        # timeout = aiohttp.ClientTimeout(total=90)
        try:
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
                    # pending2.append(asyncio.create_task(get_ting(
                        # url,lock, prop=prop,db=db, item=item, type_=type_, sem=sem, value=value, session=session, where=where)))
                    await get_ting(
                        url,lock, prop=prop,db=db, item=item, type_=type_, sem=sem, value=value, session=session, where=where)
                except:
                    pass
                bar_done.update()
                if len(pending2) > 50:
                    await asyncio.wait(pending2)
                    pending2 = []
            if len(pending2) != 0:
                await asyncio.wait(pending2)
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(
                exc_tb.tb_frame.f_code.co_filename)[1]
            


async def get_wikidata(name, prop, quarry, lock_SPRQL, db=None, type_="unknown", value_name=None, dodgy=True):
    sem = asyncio.Semaphore(5)
    things = []
    count = 0
    pending = []
    manager = get_the_manager()
    bar_done = manager.counter(total=0, desc='bar_done: '+name, unit='ticks')
    bar_start = manager.counter(total=0, desc='bar_start: '+name, unit='ticks')
    lock = asyncio.Lock()
    while True:
        try:
            async for data_i, size in SPRQL_GEN(quarry,name+".json",db=db, dodgy=dodgy):
                
                # Get URL
                bar_done.total = size
                bar_start.total = size
                count = size
                if value_name is not None:
                    url = data_i[value_name]["value"]
                else:
                    url = data_i[name]["value"]
                # if not await check_resource(url, type_, where="wikidata",db=db):
                #     bar_done.update()
                #     bar_start.update()
                #     continue
                things.append(data_i)
                bar_start.update()
                if len(things) > 100:
                    await do_thing(things, bar_done,lock,db=db, name=name, sem=sem, prop=prop, type_=type_, value_name=value_name)
                    things = []
                if count == 0:
                    continue
        except:
            continue
        return True
 

async def main_inyourarea(lock_SPRQL):
    out = {}
    postcodes =[]
    with open('/home/william/Code/Python/bod/ResourceDiscovery/alt_savices/ukpostcodes.csv', newline='') as csvfile:
        row_count = len(csvfile.readlines())
    manager = get_the_manager()
    pbar = manager.counter(total=row_count, desc='Basic', unit='ticks')
    with open('/home/william/Code/Python/bod/ResourceDiscovery/alt_savices/ukpostcodes.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in spamreader:
            postcode = i[1].replace(" ", "")
            postcodes.append(postcode)
    for i in range(10):
        postcode = random.choice(postcodes)
        while True:
            try:
                postcode = i[1].replace(" ", "")
                url_postcode = "https://production.inyourarea.co.uk/api/localPublications/{postcode}".format(
                    postcode=postcode)
                async with aiohttp.ClientSession() as session:
                    async with session.get(url_postcode) as resp:
                        data = await resp.json()
                        for site in data:
                            if postcode not in out.keys():
                                out[postcode] = [site]
                            else:
                                out[postcode].append(site)
                await sleep(25)
                pbar.update()
                break
            except BaseException as e:
                continue
        for url in out.keys():
            await get_ting("http://"+url, data=out[url],
                           type_="website", where="inyourarea")

    # "https://production.inyourarea.co.uk/facade/contentplus/50.922998/-0.749568/0?legacyPostcode=PO180HH"
    # "https://production.inyourarea.co.uk/facade/feed/PO180HH/Singleton,Charlton,West%20Dean,East%20Dean,Cocking"
    # async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(70), connector=aiohttp.TCPConnector(family=socket.AF_INET,   verify_ssl=False)) as session:
    #     async with session.post(url) as r:
    #         pass

    #     # await get_ting(url, prop=None, item=None, sem=None, data=None,
    #     #    type_="website", where="inyourarea", value=None, session=None)
    #     pass


async def main_allsides(lock_SPRQL):
    rss_website = "https://www.allsides.com/news/rss"
    site_website = "https://www.allsides.com/"
    data = {}
    for item in get_all_sides():
        if item["AllSides Bias Rating"] is not None:
            data["AllSides Bias Rating"] = item["AllSides Bias Rating"]
        if item['Community Feedback'] is not None:
            data["Community Feedback"] = item["Community Feedback"]
        if item['type'] is not None:
            data["type"] = item["type"]
        if item['Facebook Page'] is not None:
            await get_ting(item['Facebook Page'], type_="facebook",
                           where="allsides", data=data)
            pass
        if item['Twitter Page'] is not None:
            await get_ting(item['Twitter Page'], type_="twitter",
                           where="allsides", data=data)
            pass
        if item['website'] is not None:
            await get_ting(item['website'], type_="website",
                           where="allsides", data=data)
            pass


async def main_news(lock_SPRQL):
    pass


async def main_ResourceDiscovery_Q_gen(lock_SPRQL):
    manager = get_the_manager()
    aaas = []
    async for data_i, size in SPRQL_GEN(SPARQL_all_ddd,  "SPARQL_all_ddd.json"):
        Q = get_q(data_i["type_of_Wikidata_property"]["value"])
        text_ddd = SPARQL_all_fff % (Q)
        async for data_i_x2, size in SPRQL_GEN(text_ddd,  "SPARQL_all_fff.json"):
            P = get_q(data_i_x2["type_of_Wikidata_property"]["value"])
            text_ccc = SPARQL_all_cccc % (P)
            formatter_URL = data_i_x2["formatter_URL"]["value"]
            aaa.append({"text_ccc":text_ccc,"formatter_URL":formatter_URL,"P":P})
    for ix in range(10):
        aaa = random.choice(aaas)
        async for data_i_x3, size in SPRQL_GEN(aaa["text_ccc"],  "SPARQL_all_cccc.json"):
            while not await get_wikidata(name="item", type_="unknown", prop=aaa["P"], lock_SPRQL=lock_SPRQL, quarry=aaa["text_ccc"], dodgy=True):
                pass
        # formatter URL


async def UK_news_source(lock_SPRQL,db):
    connector = aiohttp.TCPConnector(family=socket.AF_INET,   verify_ssl=False)
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(70), connector=connector) as session:
        for url in news_urls:
            await get_ting(url, type_="website", where="internal", session=session,db=db)
        for url in news_left_right:
            await get_ting(url, type_="website", where="internal", session=session,db=db)


async def common_crawl_walk(lock_SPRQL,db):
    connector = aiohttp.TCPConnector(family=socket.AF_INET,   verify_ssl=False)
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(70), connector=connector) as session:
        async for i in get_some_CC():
            type_ = "unknown"
            a = urlparse(i["url"])
            url = a.scheme + "://" + a.hostname
            if "html" in i["mime"]:
                type_ = "webpage"
            elif "xml" in i["mime"]:
                url = i["url"]
                type_ = "feed"
            elif "xml" in i["mime"]:
                url = i["url"]
                type_ = "feed"
            else:
                pass
                # wen
            await get_ting(url, db=db,session=session, type_=type_, where="common crawl")


async def candidates_democracyclub():
    manager = get_the_manager()
    pbar = manager.counter(
        total=1, desc='candidates_democracyclub', unit='ticks')
    url_next = "https://candidates.democracyclub.org.uk/api/v0.9/persons/"
    ppl = {}
    while url_next is not None:
        async with aiohttp.ClientSession() as session:
            async with session.get(url_next) as resp:
                data = await resp.json()
                pbar.total = data["count"]
                for i in data["results"]:
                    id = i["id"]
                    if id not in ppl.keys():
                        ppl[id] = {}
                    # ppl[id]["gender"] = i["person"]["gender"]
                    for x in (i["memberships"]):
                        if x["elected"]:
                            ppl[id]["elected_on_behalf_of_name"] = {
                                "value": x["on_behalf_of"]["name"], "type": "Quantity"}
                            ppl[id]["elected_on_behalf_of_id"] = {
                                "value": x["on_behalf_of"]["id"], "type": "Quantity"}
                            ppl[id]["elected_post_label"] = {
                                "value": x["post"]["label"], "type": "Quantity"}
                            ppl[id]["elected_post_id"] = {
                                "value": x["post"]["id"], "type": "Quantity"}
                            ppl[id]["elected_election_id"] = {
                                "value": x["election"]["id"], "type": "Quantity"}
                            ppl[id]["elected_election_name"] = {
                                "value": x["election"]["name"], "type": "Quantity"}
                            pass
                        ppl[id]["ran_in_on_behalf_of_name"] = {
                            "value": x["on_behalf_of"]["name"], "type": "Quantity"}
                        ppl[id]["ran_in_on_behalf_of_id"] = {
                            "value": x["on_behalf_of"]["id"], "type": "Quantity"}
                        ppl[id]["ran_in_post_label"] = {
                            "value": x["post"]["label"], "type": "Quantity"}
                        ppl[id]["ran_in_post_id"] = {
                            "value": x["post"]["id"], "type": "Quantity"}
                        ppl[id]["ran_in_election_id"] = {
                            "value": x["election"]["id"], "type": "Quantity"}
                        ppl[id]["ran_in_election_name"] = {
                            "value": x["election"]["name"], "type": "Quantity"}
                    pbar.update()
                if "next" in data.keys():
                    url_next = data["next"]
                else:
                    url_next = None
    return ppl


async def data_parliament():
    pass


async def candidates_democracyclub_organizations():
    organizations = {}
    url_next = "https://candidates.democracyclub.org.uk/api/v0.9/organizations/"
    connector = aiohttp.TCPConnector(family=socket.AF_INET,   verify_ssl=False)
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(70), connector=connector) as session:
        async with session.get(url_next) as resp:
            data = await resp.json()
            for i in data["results"]:
                organizations[i["id"]] = {}

                for x in i["identifiers"]:
                    if x["scheme"] == "popit-organization":
                        pass
                        
                    elif x["scheme"] == "electoral-commission":
                        pass
                        
                    else:
                        pass
                        

                i["classification"]
                i["parent"]
                i["register"]
                i["register"]
            pass
    pass


async def main_ResourceDiscovery(name):
    lock_SPRQL = asyncio.Lock()
    db = motor_c()
    # await candidates_democracyclub()
    # await candidates_democracyclub_organizations()
    while True:
        try:
            while not await get_wikidata(name="official_website",db=db, type_="website", prop="P856", lock_SPRQL=lock_SPRQL, quarry=SPARQL_all_website):
                pass
        except:
            pass
        
        try:
            while not await get_wikidata(name="SPARQL_offical_blog",db=db, type_="blog", prop="P1581", lock_SPRQL=lock_SPRQL, quarry=SPARQL_offical_blog):
                pass
        except:
            pass
        
        try:
            while not await get_wikidata(name="SPARQL_all_feeds",db=db, type_="feed", prop="P1019", lock_SPRQL=lock_SPRQL, quarry=SPARQL_all_feeds):
                pass
        except:
            pass
        await common_crawl_walk(lock_SPRQL,db)
        await UK_news_source(lock_SPRQL,db)
        await main_inyourarea(lock_SPRQL,db)
        await main_ResourceDiscovery_Q_gen(lock_SPRQL,db)
