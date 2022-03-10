import asyncio
from re import T
from uitls.asyncio_c import wait_task
from uitls.web_wehsite import add_other_parameter, url_add
from scrape_service.wikidata import Get_Q, SPARQL_all_feeds, SPARQL_all_website, SPARQL_offical_blog, Wikidata_qurry_property, sprql_wikidata

import enlighten


def main():
    pass

sem_c = asyncio.BoundedSemaphore(60)  
manager = enlighten.Manager()
async def get_wikidata_website(data_p):
    a =[]
    datas = await sprql_wikidata(SPARQL_all_website)
    pbar = manager.counter(desc='get_wikidata_website', total=len(datas))
    starting_good = pbar.add_subcounter('green')
    started_bad = pbar.add_subcounter('red')
    async def k(data,item,data_ps):
         async with  sem_c:
            if await url_add(data, "wikidata", item,Ps=data_ps):
                starting_good.update()
            else:
                started_bad.update()
                print("has bad")
    for data in datas:
        data["item"]=Get_Q(data["item"])
    for data in datas:
        a.append(k(data["official_website"],data["item"],data_p))
    await wait_task(a)

async def get_wikidata_feed(data_p):
    a =[]
    datas = await sprql_wikidata(SPARQL_all_feeds)
    pbar = manager.counter(desc='get_wikidata_feed',total=len(datas))
    starting_good = pbar.add_subcounter('green')
    started_bad = pbar.add_subcounter('red')
    async def k(data,item,data_ps):
        async with  sem_c:
            if await url_add(data, "wikidata", item,Ps=data_ps):
                starting_good.update()
            else:
                started_bad.update()
            pbar.update()
    for data in datas:
        data["item"]=Get_Q(data["item"])
    for data in datas:
        if "web_feed_URL" in data.keys():
            a.append(k(data["web_feed_URL"],data["item"],data_p))
    await wait_task(a)

async def get_wikidata_blog(data_p):
    a =[]
    datas = await sprql_wikidata(SPARQL_offical_blog)
    pbar = manager.counter(desc='get_wikidata_blog',total=len(datas))
    starting_good = pbar.add_subcounter('green')
    started_bad = pbar.add_subcounter('red')
    async def k(data,item,data_ps):
        async with  sem_c:
            if await url_add(data, "wikidata", item,Ps=data_ps):
                starting_good.update()
            else:
                started_bad.update()
    for data in datas:
        data["item"]=Get_Q(data["item"])
    for data in datas:
        if "official_blog" in data.keys():
            a.append(k(data["official_blog"],data["item"],data_p))
    await wait_task(a)
async def get_wikidata_other_parameter():
    datas_ = {}
    print("geting wikidata_other_parameter")
    datas = await sprql_wikidata(Wikidata_qurry_property)
    print("done wikidata_other_parameter")
    pbar = manager.counter(desc='get_wikidata_other_parameter',total=len(datas))

    for data in datas:
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
    print("geting add_other_parameter")
    return datas_

async def get_other_parameter_scan(datas):
    pbar = manager.counter(desc='get_other_parameter_scan',total=len(datas))
    starting_good = pbar.add_subcounter('yellow')
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
            async with  sem_c:
                if True:
                    starting_good.update()
                else:
                    started_bad.update()
                return 
            lllx.append(k(query, datas[P]))
    vs = await wait_task(lllx)

async def get_common_crawl_website():
    async def k():
        pass
    url_add(url_from, where, item=None)


async def get_common_crawl_feed():
    async def k():
        pass
    pass


async def get_web_archive_website():
    async def k():
        pass
    url_add(url_from, where, item=None)


async def get_web_archive_feed():
    async def k():
        pass
    pass

async def main():
    data = await get_wikidata_other_parameter()
    a = [
        get_wikidata_website(data),
        # get_wikidata_feed(data),
        # get_wikidata_blog(data),
        # get_other_parameter_scan(data),
    ]
    await wait_task(a)
    
async def test():
    await get_wikidata_feed()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
