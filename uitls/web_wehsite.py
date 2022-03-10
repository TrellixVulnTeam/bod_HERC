import asyncio
import tldextract
from rfc3986 import urlparse
from uitls.AsyncRobot import Robot
from uitls.asyncio_c import wait_task
from uitls.feedCheck import feedCheck
from uitls.get import aio_check_if_page_exists, async_check_if_website_exists
from uitls.scan_f import scanHTML
from scrape_service.wikidata import wikidata_linked, Get_Q, sprql_wikidata
import motor.motor_asyncio
from datetime import datetime
myclient = motor.motor_asyncio.AsyncIOMotorClient()

scrap = myclient.scrap
websiteDb = scrap.website
feedTypes_ends = [
    'feed+json',
    'rss+xml',
    'rss',
    'atom+xml',
    'atom',
    "json"
]


async def remove_website_where(url_from, where=None, path=None, item=None):
    myquery = {
        "url_from": url_from
    }
    if await websiteDb.find(myquery) is not None:
        if item is None:
            test = await websiteDb.remove(myquery)
        else:
            test = await websiteDb.remove(myquery)


async def add_website_where(url_to, where, path, type_="website", item=None, mps={}):
    myquery1 = {
        "to_url": url_to,
        "points": { "$elemMatch":{
        "where": where,
        "path": path,
        "type": type_,
        }
        }
    }
    myquery2 = {
        "to_url": url_to,
        "points": { "$elemMatch":{
        "where": where,
        "path": path,
        "type": type_,
        }
        }
    }
    myquery3 = {
        "to_url": url_to,
    }
    
    data_website_pill =  {"points": {'$pull': {
            "where":where,
            "path":path,
            "type":type_
    }}}
    data_website =  {"points": {'$push': {
            "where":where,
            "path":path,
            "type":type_
    }}}
    if item is not None:
        myquery1["points"]["$elemMatch"]["ID"] = item
        myquery2["points"]["$push"]["ID"] = item
        data_website["points"]["$push"]["ID"] = item
        data_website_pill["points"]["$pull"]["ID"] = item
    if where == "wikidata":
        data = await wikidata_linked(Get_Q(item), mps)
        myquery1["points"]["$elemMatch"]["data"] = data
        data_website["points"]["$push"]["data"] = data
        
    print(myquery1)
    c = await websiteDb.find_one(myquery1)
    print(c)
    if c is not None:
        return
    c = await websiteDb.find_one(myquery2)
    print(c)
    if c is not None:
        await websiteDb.update_one(myquery2,data_website_pill)
        await websiteDb.update_one(myquery2,data_website)
    else:
        await websiteDb.update_one(myquery3,data_website)

async def _add_wensite_(url_to, url_from):
    myquery1 = {"to_url": url_to }
    c = await websiteDb.find_one(myquery1)
    if (c) is not None:
        myquery2 = {"url_from": url_from}
        c = await websiteDb.find_one(myquery2)
        if (c) is not None:
            pass
        else:  
            data_website = { "$push": {"url_from": url_from}}
            await websiteDb.update_one(myquery2,data_website)
    else:
        data_website = {
            "to_url": url_to,
            "url_from":[ url_from],
            "points":[],
        }
        await websiteDb.insert_one(data_website)

async def _add_wensite_(url_to, url_from):
    url_to = str(url_to)
    if (await websiteDb.find_one({"to_url": url_to, "from_url": url_from})) is not None:
        print("need to url")
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
        print("need add url from")
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
    await url_add(data["href"], where="internal", item_type="websub")


async def url_add(url_from, where, item=None, item_type="website", dectect_item_type=True, Ps={}):
    url_from = str(url_from)
    check, _, x = urlCheck(url_from)
    url_parts = urlparse(url_from)
    if not check:
        return False
    check, url_to, text, mine, path, status = await async_check_if_website_exists(url_from)
    if not check:
        check, url_to, text, mine, path, status = await aio_check_if_page_exists(url_from)
        if not check:
            return False
    if (url_parts.path != "/" and url_parts.path != "") or item_type != "website":
        check, url_to, text, mine, path_, status = await aio_check_if_page_exists(url_from)
        if not check:
            item = None
        if check and dectect_item_type:
            item_type = "page"
    # check, datas = feedCheck(text)
    call_async = []
    # for data in datas:
    #     if "feed" == data["type"]:
    #         call_async.append(feed_do(data))
    #     elif "hub" == data["type"]:
    #         call_async.append(websub_do(data))
    # if  check and dectect_item_type:
    #     item_type="feed"
    await _add_wensite_(url_to, url_from)
    await add_website_where(url_to, where, path,item_type , item,Ps)
    await scanHTML(text, url_to)
    # await wait_task(call_async)
    return True


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
