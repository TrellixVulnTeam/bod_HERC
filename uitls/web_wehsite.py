import asyncio
import tldextract
from rfc3986 import urlparse
from uitls.AsyncRobot import Robot
from uitls.feedCheck import feedCheck
from uitls.get import aio_check_if_page_exists, async_check_if_website_exists
from uitls.scan_f import scanHTML
from scrape_service.wikidata import wikidata_linked, Get_Q ,sprql_wikidata
import motor.motor_asyncio
from datetime import datetime
myclient = motor.motor_asyncio.AsyncIOMotorClient()

scrap = myclient.scrap
websiteDb =scrap.website

async def _add_wensite_(url_to, url_from):
    if websiteDb.find({"to_url": url_to, "from_url": url_from}) is not None:
        pass
    elif websiteDb.find({"url_from": url_from}) is not None:
        myquery = {
            "to_url": url_to
        }
        newvalues = {
            "$push": {
                "url_from": url_from
            }
        }
        await websiteDb.update_one(myquery, newvalues)

    else:
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
        await websiteDb.update_one(myquery, data_website)


async def extract_url(url):
    while True:
        try:
            ext = tldextract.extract(url)
            return ext
        except:
            await asyncio.sleep(10)


def urlCheck(url):
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
    mydb = myclient["scrap"]
    mycol = mydb.wikidata
    lll = []
    for P in datas:
        async def k(query,data_):
            items = await sprql_wikidata(query)
            for item in items:
                print(item)
        query = """
        SELECT ?item ?itemLabel ?data WHERE {
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
          { ?item wdt:"""+P+""" ?data. }
        }
        """
        lll.append(k(query,datas[P]))
    asyncio.gather(*lll)


async def url_add(url_from, where, item=None):
    check, _ , x= urlCheck(url_from)
    if not check:
        return False
    check, url_to, text, mine, path = await async_check_if_website_exists(url_from)
    if not check:
        check, url_to, text, mine, path = await async_check_if_website_exists(url_from)
        if not check:
            print("failed")
            return False
    
    await _add_wensite_(url_to, url_from)
    if where == "wikidata":
        myquery = {
            "to_url": url_to
        }
        newvalues = {
            "$push": {"date":  {
                "time": datetime.now(),
                "type": "website",
                "where": where,
                "item": item,
                "path": path,
                "data": await wikidata_linked(Get_Q(item)),
            }}}
        await websiteDb.update_one(myquery, newvalues)
    elif where == "dbpedia":
        newvalues = {
            "$push": {"date":  {
                "time": datetime.now(),
                "type": "website",
                "where": where,
                "path": path
            }}}
        await scrap.update_one(myquery, newvalues)
    elif where == "wayback":
        newvalues = {
            "$push": {"date":  {
                "time": datetime.now(),
                "type": "website",
                "where": where,
                "path": path
            }}}
        await websiteDb.update_one(myquery, newvalues)
    elif where == "commoncrawl":
        newvalues = {
            "$push": {"date":  {
                "time": datetime.now(),
                "type": "website",
                "where": where,
                "path": path
            }}}
        await websiteDb.update_one(myquery, newvalues)
    await scanHTML(text, url_to)


async def url_feed(url_from, item=None, where=None):
    check, _ , x = urlCheck(url_from)
    if not check:
        return False
    check, url_to, text, mine, path = await aio_check_if_page_exists(url_from)
    if not check:
        return False
    check, urls = feedCheck(text)
    if not check:
        return False
    await _add_wensite_(url_to, url_from)
    if item is not None:
        if where == "wikidata":
            myquery = {
                "to_url": url_to
            }
            newvalues = {
                "$push": {"date":  {
                    "time": datetime.now(),
                    "type": "feed",
                    "where": where,
                    "item": item,
                    "path": path,
                    "data": await wikidata_linked(Get_Q(item)),
                }}}
            await websiteDb.update_one(myquery, newvalues)
        elif where == "dbpedia":
            myquery = {
                "to_url": url_to
            }
            newvalues = {
                "$push": {"date":  {
                    "time": datetime.now(),
                    "type": "feed",
                    "where": where,
                    "path": path,
                    "url_from": url_from,
                    "url_from": url_to,
                }}}
            await websiteDb.update_one(myquery, newvalues)
        elif where == "commoncrawl" or where == "wayback":
            myquery = {
                "to_url": url_to
            }
            newvalues = {
                "$push": {"date":  {
                    "time": datetime.now(),
                    "type": "feed",
                    "where": where,
                    "path": path,
                }}}
            await websiteDb.update_one(myquery, newvalues)


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
