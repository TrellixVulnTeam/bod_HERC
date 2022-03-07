import asyncio
from uitls.web_wehsite import add_other_parameter, url_add
from scrape_service.wikidata import Get_Q, SPARQL_all_feeds, SPARQL_all_website, SPARQL_offical_blog, Wikidata_qurry_property, sprql_wikidata


def main():
    pass


async def get_wikidata_website():
    a =[]
    datas = await sprql_wikidata(SPARQL_all_website)
    for data in datas:
        data["item"]=Get_Q(data["item"])
    for data in datas:
        a.append(url_add(data["official_website"], "wikidata", item=data["item"]))
    await asyncio.wait(a)

async def get_wikidata_feed():
    a =[]
    datas = await sprql_wikidata(SPARQL_offical_blog)
    for data in datas:
        data["item"]=Get_Q(data["item"])
    for data in datas:
        a.append(url_add(data["official_blog"], "wikidata", item=data["item"]))
    await asyncio.wait(a)

async def get_wikidata_blog():
    a =[]
    datas = await sprql_wikidata(SPARQL_all_feeds)
    for data in datas:
        data["item"]=Get_Q(data["item"])
    for data in datas:
        a.append(url_add(data["web_feed_URL"], "wikidata", item=data["item"]))
    await asyncio.wait(a)

async def get_wikidata_other_parameter():
    datas_ = {}
    print("geting wikidata_other_parameter")
    datas = await sprql_wikidata(Wikidata_qurry_property)
    print("done wikidata_other_parameter")
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
    await add_other_parameter(datas_)


async def get_common_crawl_website():
    url_add(url_from, where, item=None)


async def get_common_crawl_feed():
    pass


async def get_web_archive_website():
    url_add(url_from, where, item=None)


async def get_web_archive_feed():
    pass
# url_feed(url, item_=None, where=None)


async def test():
    await get_wikidata_feed()
loop = asyncio.get_event_loop()
loop.run_until_complete(test())
