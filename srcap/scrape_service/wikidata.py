from qwikidata import typedefs
import asyncio
import time
from uitls.SPRQL import SPRQL_GEN
from qwikidata.entity import WikidataItem, WikidataLexeme, WikidataProperty
from qwikidata.datavalue import WikibaseEntityId, Time, Quantity, GlobeCoordinate

import motor.motor_asyncio
data_sprql = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"


myclient = motor.motor_asyncio.AsyncIOMotorClient()

scrap = myclient.scrap
wikidataDb = scrap.wikidata


async def sprql_wikidata(qurry, file_name):
    return SPRQL_GEN(qurry, data_sprql, file_name, online=True)


def get_q(Q):
    Q = Q.replace(
        "https://www.wikidata.org/entity/", "")
    Q = Q.replace(
        "http://www.wikidata.org/entity/", "")
    return Q


WIKIDATA_LDI_URL = "https://www.wikidata.org/wiki/Special:EntityData"


async def aio_get_entity_dict_from_api2(entity_id: typedefs.EntityId, base_url: str = WIKIDATA_LDI_URL, session=None) -> typedefs.EntityDict:
    url = "{}/{}.json".format(base_url, entity_id)
    for i in range(100):
        async with session.post(url) as response:
            if response.ok:
                entity_dict_full = await response.json()
            else:
                continue

            # remove redundant top level keys
            returned_entity_id = next(iter(entity_dict_full["entities"]))
            entity_dict = entity_dict_full["entities"][returned_entity_id]
            return entity_dict
    raise None


async def __aio_get_entity_dict_from_api(Q, session=None):
    q_dict = wikidataDb.find_one({'title': Q})
    if (q_dict is None) or ("daedtime" not in q_dict.keys()):
        q_dict = await aio_get_entity_dict_from_api2(Q, session=session)
        q_dict["daedtime"] = (86400*30) + int(time.time())
        wikidataDb.insert_one(q_dict)
    q_ = WikidataItem(q_dict)
    return q_, q_dict


async def wikidata_linked(Q, magic=[], session=None):
    dos = []
    data = []
    q_, q_dict = await __aio_get_entity_dict_from_api(Q, session=session)
    claim_groups = q_.get_truthy_claim_groups()
    for claim in q_dict["claims"]:
        claims = claim_groups[claim]
        if len(claims) > 0:
            for claim in claims:
                try:
                    if isinstance(claim.mainsnak.datavalue, GlobeCoordinate):
                        value = claim.mainsnak.datavalue.value
                    elif isinstance(claim.mainsnak.datavalue, Time):
                        value = claim.mainsnak.datavalue.value
                        data.append({claim.property_id: value['time']})
                        continue
                    elif isinstance(claim.mainsnak.datavalue, WikibaseEntityId):
                        value = claim.mainsnak.datavalue.value
                        data.append({claim.property_id: value['id']})
                        continue
                    elif claim.property_id in magic:
                        value = claim.mainsnak.datavalue.value
                        if "formatter_URL" in magic[claim.property_id].keys():
                            for formatter_URL in magic[claim.property_id]["formatter_URL"]:
                                url = formatter_URL.replace("$1", value)
                                dos.append(url)
                except:
                    pass
    return data, dos


SPARQL_all_website = """
SELECT * WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  { ?item wdt:P856 ?official_website. }
}
"""
SPARQL_offical_blog = """
SELECT * WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  OPTIONAL { ?item wdt:P1581 ?official_blog. }
}
"""
SPARQL_all_feeds = """
SELECT * WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    OPTIONAL {?item wdt:P1019 ?web_feed_URL.}
}
"""
Wikidata_qurry_property3 = """
SELECT DISTINCT ?item ?itemLabel ?maintained_by ?maintained_byLabel ?formatter_URL WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  { ?item wdt:P7250 ?mobile_formatter_URL. }
  UNION
  { ?item wdt:P1630 ?formatter_URL. }
  UNION
  { ?item wdt:P8966 ?URL_match_pattern. }
  UNION
  { ?item wdt:P3303 ?third_party_formatter_URL. }
  UNION
  { ?item wdt:P1896 ?source_website_for_the_property. }
  UNION
  { ?item wdt:P1793 ?format_as_a_regular_expression. }
  UNION
  { ?item wdt:P1630 ?formatter_URL. }
  {
    { ?item wdt:P2378 ?maintained_by. }
    UNION
    { ?item wdt:P126 ?maintained_by. }
    UNION
    { ?item wdt:P9073 ?maintained_by. }
    UNION
    { ?item wdt:P1629 ?maintained_by. }
    UNION
    { ?item wdt:P2378 ?maintained_by. }
  }
  OPTIONAL { ?item wdt:P1630 ?formatter_URL. }
}
"""
Wikidata_qurry_property2 = """
SELECT DISTINCT ?item ?itemLabel ?maintained_by ?maintained_byLabel ?formatter_URL WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  { ?item wdt:P7250 ?mobile_formatter_URL. }
  UNION
  { ?item wdt:P1630 ?formatter_URL. }
  UNION
  { ?item wdt:P8966 ?URL_match_pattern. }
  UNION
  { ?item wdt:P3303 ?third_party_formatter_URL. }
  UNION
  { ?item wdt:P1896 ?source_website_for_the_property. }
  UNION
  { ?item wdt:P1793 ?format_as_a_regular_expression. }
  UNION
  { ?item wdt:P1630 ?formatter_URL. }
  {
    { ?item wdt:P2378 ?maintained_by. }
    UNION
    { ?item wdt:P126 ?maintained_by. }
    UNION
    { ?item wdt:P9073 ?maintained_by. }
    UNION
    { ?item wdt:P1629 ?maintained_by. }
    UNION
    { ?item wdt:P2378 ?maintained_by. }
  }
  OPTIONAL { ?item wdt:P1630 ?formatter_URL. }
}
"""

Wikidata_qurry_property = """
SELECT DISTINCT ?formatter_URL ?URL_match_pattern ?Wikidata_property ?Wikidata_propertyLabel ?maintained_by ?maintained_byLabel    ?mobile_formatter_URLitem ?third_party_formatter_URL ?Wikidata_property_to_identify_online_accounts ?Wikidata_property_to_identify_online_accountsLabel WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  { ?Wikidata_property wdt:P31 wd:Q62589320. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q93433126. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q62589316. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q105388954. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q21745557. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55452870. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q24075706. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q21745557. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q18618628. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q19595382. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q102348160. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q96776953. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q84612171. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q68573177. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q52063969. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q105946994. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q42415497. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q27048688. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q26883022. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q26696664. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q24575337. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q107737561. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q107737592. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q107737623. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q107737660. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q42415497. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q42396390. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q27048688. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q26883022. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q24075706. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q23673786. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q22965078. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q28146956. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q107095360. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q100391350. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q67042573. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66117735. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66116790. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66116613. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q22964274. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66480643. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q64742143. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55663533. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q29542094. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66116790. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66480643. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q101081817. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q106035765. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q100698536. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66118402. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66117915. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q56505345. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q56245078. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q19833835. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q19833835. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q19833377. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q107786704. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q107235145. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q101083593. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q57589544. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55999460. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55663533. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q44847669. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q29547399. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q29542094. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q28916621. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q107786704. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q110953035. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q110953039. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q110953042. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66118402. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66117915. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q19833377. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q56245078. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q19829908. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q28916621. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q108884050. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q108765768. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q103979805. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q102357699. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q100698536. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q56505345. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q56249389. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q56245078. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q45484922. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q19829908. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q102357699. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q106839109. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q106702532. }
  UNION
  { ?Wikidata_property wdt:P279 wd:Q66626337. }
  UNION
  { ?Wikidata_property wdt:P279 wd:Q66626337. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55978551. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55978503. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55978235. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55977691. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q42428590. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q28916621. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q19595382. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q107211056. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q106653189. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q97584729. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q93436926. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q93436926. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q93433126. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q88206155. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66712599. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q66118387. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q64742143. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55653847. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q55650689. }
  UNION
  { ?Wikidata_property wdt:P31 wd:Q27870307. }
  
  { ?Wikidata_property wdt:P9073 ?maintained_by. }
  UNION
  { ?Wikidata_property wdt:P1629 ?maintained_by. }
  UNION
  { ?Wikidata_property wdt:P2378 ?maintained_by. }
  UNION
  { ?Wikidata_property wdt:P126 ?maintained_by. }
  
  OPTIONAL { ?Wikidata_property wdt:P1630 ?formatter_URL. }
  OPTIONAL { ?Wikidata_property wdt:P8966 ?URL_match_pattern. }
}
"""
