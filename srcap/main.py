import asyncio
import os
from re import T
import socket
import sys

import aiohttp
from scrape_service.commoncrawl import commoncrawl_init, get_common_crawl_reqest_pages
from uitls.AsyncResolver2 import AsyncResolver2
from uitls.asyncio_c import wait_task
from uitls.web_wehsite import add_other_parameter, url_add
from scrape_service.wikidata import Get_Q, SPARQL_all_feeds, SPARQL_all_website, SPARQL_offical_blog, Wikidata_qurry_property, sprql_wikidata
from scrape_service.commoncrawl import toplevels
import enlighten
import gc


def main():
    pass


manager = enlighten.Manager()


async def get_wikidata_website(data_p, session):
    pedding = []
    gc.collect()
    pbar = manager.counter(desc='get_wikidata_website', total=0)
    pbar_started = manager.counter(
        desc='get_wikidata_website started', total=len([]))
    starting_good = pbar.add_subcounter('green')
    started_bad = pbar.add_subcounter('yellow')
    started_error = pbar.add_subcounter('red')

    async def k(data, item, data_ps):
        try:
            pbar_started.update()
            if await url_add(data, "wikidata", item, Ps=data_ps, session=session):
                starting_good.update()
            else:
                started_bad.update()
        except:
            started_error.update()
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("ERROR ", (exc_obj), ":", type(exc_obj),
                  exc_type, fname, exc_tb.tb_lineno)
        gc.collect()
    data = await sprql_wikidata(SPARQL_all_website, "SPARQL_all_website.json")
    cont = 0
    async for data, size in data:
        pbar.total = size
        pbar_started.total = size
        cont = cont + 1
        pedding.append(asyncio.create_task(k(data["official_website"]["value"],
                                             Get_Q(data["item"]["value"]), data_p)))
        while cont > 1000:
            try:
                await asyncio.sleep(1.0)
                done, pedding = await asyncio.wait(pedding, timeout=1.0)
                cont = cont - len(done)
                pedding = list(pedding)
            except:
                pass
    await asyncio.wait(pedding)


async def get_wikidata_feed(data_p, session):
    a = []
    gc.collect()
    datas = await sprql_wikidata(SPARQL_all_feeds, session)
    gc.collect()
    pbar = manager.counter(desc='get_wikidata_feed', total=len(datas))
    starting_good = pbar.add_subcounter('green')
    started_bad = pbar.add_subcounter('red')

    async def k(data, item, data_ps):

        try:
            if await url_add(data, "wikidata", item, Ps=data_ps, session=session):
                starting_good.update()
            else:
                started_bad.update()
        except:
            started_bad.update()
        gc.collect()

    for data in datas:
        data["item"] = Get_Q(data["item"])
    for data in datas:
        if "web_feed_URL" in data.keys():
            a.append(k(data["web_feed_URL"], data["item"], data_p))
    await wait_task(a)


async def get_wikidata_blog(data_p, session):
    a = []
    gc.collect()
    datas = await sprql_wikidata(SPARQL_offical_blog, session)
    gc.collect()
    pbar = manager.counter(desc='get_wikidata_blog', total=len(datas))
    starting_good = pbar.add_subcounter('green')
    started_bad = pbar.add_subcounter('red')

    async def k(data, item, data_ps):

        try:
            if await url_add(data, "wikidata", item, Ps=data_ps, session=session):
                starting_good.update()
            else:
                started_bad.update()
        except:
            started_bad.update()
        gc.collect()
    for data in datas:
        data["item"] = Get_Q(data["item"])
    for data in datas:
        if "official_blog" in data.keys():
            a.append(k(data["official_blog"], data["item"], data_p))
    await wait_task(a)


async def get_wikidata_other_parameter():
    datas_ = {}
    print("geting wikidata_other_parameter")
    print("done wikidata_other_parameter")
    pbar = manager.counter(
        desc='get_wikidata_other_parameter', total=0)

    for data, size in sprql_wikidata(Wikidata_qurry_property):
        pbar.total = size
        data["Wikidata_property"] = Get_Q(data["Wikidata_property"])
        if data["Wikidata_property"] not in datas_.keys():
            datas_[data["Wikidata_property"]] = {
                "Wikidata_property": data["Wikidata_property"],
            }
        if "formatter_URL" in data.keys():
            if "formatter_URL" not in datas_[data["Wikidata_property"]].keys():
                datas_[data["Wikidata_property"]]["formatter_URL"] = []
            if data["formatter_URL"] not in datas_[data["Wikidata_property"]]["formatter_URL"]:
                datas_[data["Wikidata_property"]]["formatter_URL"].append(
                    data["formatter_URL"])
        if "URL_match_pattern" in data.keys():
            if "URL_match_pattern" not in datas_[data["Wikidata_property"]].keys():
                datas_[data["Wikidata_property"]]["URL_match_pattern"] = []
            if data["URL_match_pattern"] not in datas_[data["Wikidata_property"]]["URL_match_pattern"]:
                datas_[data["Wikidata_property"]]["URL_match_pattern"].append(
                    data["URL_match_pattern"])
        if "Wikidata_propertyLabel" in data.keys():
            if "Wikidata_propertyLabel" not in datas_[data["Wikidata_property"]].keys():
                datas_[data["Wikidata_property"]
                       ]["Wikidata_propertyLabel"] = ""
            if data["Wikidata_propertyLabel"] not in datas_[data["Wikidata_property"]]["Wikidata_propertyLabel"]:
                datas_[data["Wikidata_property"]]["Wikidata_propertyLabel"] = (
                    data["Wikidata_propertyLabel"])

        if "maintained_by" in data.keys():
            if "maintained_by" not in datas_[data["Wikidata_property"]].keys():
                datas_[data["Wikidata_property"]]["maintained_by"] = ""
            if Get_Q(data["maintained_by"]) not in datas_[data["Wikidata_property"]]["maintained_by"]:
                datas_[data["Wikidata_property"]]["maintained_by"] = Get_Q(
                    data["maintained_by"])
        if "mobile_formatter_URLitem" in data.keys():
            if "mobile_formatter_URLitem" not in datas_[data["Wikidata_property"]].keys():
                datas_[data["Wikidata_property"]
                       ]["mobile_formatter_URLitem"] = []
            if data["mobile_formatter_URLitem"] not in datas_[data["Wikidata_property"]]["mobile_formatter_URLitem"]:
                datas_[data["Wikidata_property"]]["mobile_formatter_URLitem"].append(
                    data["mobile_formatter_URLitem"])
        if "third_party_formatter_URL" in data.keys():
            if "third_party_formatter_URL" not in datas_[data["Wikidata_property"]].keys():
                datas_[data["Wikidata_property"]
                       ]["third_party_formatter_URL"] = []
            if data["third_party_formatter_URL"] not in datas_[data["Wikidata_property"]]["third_party_formatter_URL"]:
                datas_[data["Wikidata_property"]]["third_party_formatter_URL"].append(
                    data["third_party_formatter_URL"])
        if "Wikidata_property_to_identify_online_accounts" in data.keys():
            if "Wikidata_property_to_identify_online_accounts" not in datas_[data["Wikidata_property"]].keys():
                datas_[data["Wikidata_property"]
                       ]["Wikidata_property_to_identify_online_accounts"] = []
            if data["Wikidata_property_to_identify_online_accounts"] not in datas_[data["Wikidata_property"]]["Wikidata_property_to_identify_online_accounts"]:
                datas_[data["Wikidata_property"]]["Wikidata_property_to_identify_online_accounts"].append(
                    data["Wikidata_property_to_identify_online_accounts"])
        if "Wikidata_property_to_identify_online_accountsLabel" in data.keys():
            if "Wikidata_property_to_identify_online_accountsLabel" not in datas_[data["Wikidata_property"]].keys():
                datas_["Wikidata_property_to_identify_online_accountsLabel"] = ""
            if data["Wikidata_property_to_identify_online_accountsLabel"] not in datas_[data["Wikidata_property"]]["Wikidata_property_to_identify_online_accountsLabel"]:
                datas_[data["Wikidata_property"]]["Wikidata_property_to_identify_online_accountsLabel"] = (
                    data["Wikidata_property_to_identify_online_accountsLabel"])
        pbar.update()
    print("geting add_other_parameter")
    return datas_


async def get_other_parameter_scan(datas, session):
    gc.collect()
    pbar = manager.counter(desc='get_other_parameter_scan', total=0)
    starting_good = pbar.add_subcounter('green')
    started_bad = pbar.add_subcounter('red')
    lllx = []
    for P in datas:
        query = """
        SELECT ?item ?itemLabel ?data WHERE {
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
          { ?item wdt:"""+P+""" ?data. }
        }
        """

        async def k(query, data_p):
            async def c(url, data2):

                try:
                    if await url_add(url, "wikidata", data2, Ps={}, session=session):
                        starting_good.update()
                    else:
                        started_bad.update()
                except:
                    started_bad.update()
                gc.collect()

            az = []
            if "formatter_URL" in data_p.keys():
                for formatter_URL in data_p["formatter_URL"]:
                    datas = await sprql_wikidata(query)
                    for data in datas:
                        url = formatter_URL.replace("$1", data["data"])
                        az.append(c(url, Get_Q(data["item"])))
            elif "third_party_formatter_URL" in data_p.keys():
                pass
            else:
                pass
            pbar.total = pbar.total + len(az)
            await wait_task(az)
            return
        lllx.append(k(query, datas[P]))
    await wait_task(lllx)


async def get_common_crawl_website(data_commoncrawl, session):
    cc = []
    for data_commoncrawl in data_commoncrawl:
        for toplevel in toplevels:
            params1 = [
                ('url', toplevel),
                ('matchType', 'domain'),
                ('filter', 'status'),
            ]
            params2 = [
                ('url', toplevel),
                ('matchType', 'domain'),
                ('filter', 'status'),
                ('showNumPages', 'true'),
            ]
            cc.append(get_common_crawl_reqest_pages(
                data_commoncrawl, params1, params2, session=session))
    await wait_task(cc)


async def get_web_archive_website_feed(data_commoncrawl, session):
    cc = []
    pbar = manager.counter(desc='get_web_archive_website_feed', total=len([]))
    starting_good = pbar.add_subcounter('green')
    started_bad = pbar.add_subcounter('red')
    for data_commoncrawl in data_commoncrawl:
        for toplevel in toplevels:
            params1 = [
                ('url', toplevel),
                ('matchType', 'domain'),
                ('filter', 'mime:~*/xml'),
            ]
            params2 = [
                ('url', toplevel),
                ('filter', 'mime:~*/xml'),
                ('matchType', 'domain'),
                ('showNumPages', 'true'),
            ]
            cc.append(get_common_crawl_reqest_pages(
                data_commoncrawl, params1, params2, session=session))
    await wait_task(cc)


async def main():
    # data_wikidata = await get_wikidata_other_parameter()
    data_wikidata = {}
    # data_commoncrawl = await commoncrawl_init()
    data_commoncrawl = {}
    resolver = aiohttp.AsyncResolver()
    timeout = aiohttp.ClientTimeout(total=60)
    print("cats")
    c = aiohttp.TCPConnector(limit=555, ssl=False,
                             family=socket.AF_INET, resolver=resolver)
    print("cats")
    async with aiohttp.ClientSession(connector=c, trust_env=True, timeout=timeout) as session:
        print("cats")
        await get_wikidata_website(data_wikidata, session)
        # print("cats")
        # await get_wikidata_feed(data_wikidata,session)
        # print("cats")
        # await get_wikidata_blog(data_wikidata,session)
        # print("cats")
        # await get_other_parameter_scan(data_wikidata,session)
        # print("cats")
        # await get_common_crawl_website(data_commoncrawl,session)
        # print("cats")
        # await get_web_archive_website_feed(data_commoncrawl,session)
        # print("cats")


async def test():
    await get_wikidata_feed()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
