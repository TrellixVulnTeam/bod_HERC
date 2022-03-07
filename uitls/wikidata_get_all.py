
import asyncio
from ipaddress import collapse_addresses
import json
import requests
from alive_progress import alive_bar
import time
import enlighten
from torch import conv_tbc
import motor.motor_asyncio
import SPRQL
from qwikidata.entity import WikidataItem, WikidataLexeme, WikidataProperty
from qwikidata.linked_data_interface import aio_get_entity_dict_from_api
manager = enlighten.get_manager()





myclient = motor.motor_asyncio.AsyncIOMotorClient()
async def main():
    mydb = myclient["scrap"]
    mycol = mydb.wikidata
    tasks = []
    sp = SPRQL(Wikidata_qurry_property,
               "https://query.wikidata.org/bigdata/namespace/wdq/sparql")
    data = await sp.run()
    bar = manager.counter(total=len(data), desc='P', unit='ticks')
    for i in data:
            P = i["Wikidata_property"].replace(
                "http://www.wikidata.org/entity/", "")
            # if P in p_list:
            #     bar()
            #     continue
            # p_list.append(P)
            data2 = """
        SELECT ?item ?itemLabel ?data WHERE {
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
          { ?item wdt:"""+P+""" ?data. }
        }
        """
            async def k():
                try:
                    items = await sp.run(10,data2)
                    if len(items) == 0:
                        return
                    if items is None:
                        return
                    for item in items:
                        myquery = {
                                "item": item["item"],
                                "itemLabel": item["itemLabel"],
                        }
                        newvalues = {
                                "item": item["item"],
                                "itemLabel": item["itemLabel"],
                                i["Wikidata_propertyLabel"]: item["data"]
                        }
                        if await mycol.find_one(newvalues)  is not None:
                            pass
                        elif await mycol.find_one(myquery) is None:
                            await mycol.insert_one ( newvalues)
                            Q = item["item"].replace(
                                "https://www.wikidata.org/entity/", "")
                            Q =  Q.replace(
                                "http://www.wikidata.org/entity/", "")
                            q_dict = await aio_get_entity_dict_from_api(Q)
                            print("dict:",q_dict)
                            q_ = WikidataItem(q_dict)
                            claim_groups = q_.get_truthy_claim_groups()
                            for claim in q_dict["claims"]:
                                p69_claim_group = claim_groups[claim]
                                if len(p69_claim_group) > 0:
                                    for ix in p69_claim_group:
                                        pass
                                else:
                                        pass
    
                        else:
                            d = {
                                "item": item["item"],
                                "itemLabel": item["itemLabel"],
                                i["Wikidata_propertyLabel"]: item["data"]
                            }
                            await mycol.update_one(myquery, {"$set":d})
                except Exception as e:
                    print(e)
                
                bar.update()
            tasks.append(k())
    await asyncio.gather(*tasks)

async def main():
    mydb = myclient["scrap"]
    mycol = mydb.wikidata
    tasks = []
    sp = SPRQL(Wikidata_qurry_property,
               "https://query.wikidata.org/bigdata/namespace/wdq/sparql")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
