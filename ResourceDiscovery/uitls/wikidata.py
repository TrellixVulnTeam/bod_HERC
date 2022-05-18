import sys
from qwikidata import typedefs
import asyncio
import time
from qwikidata.entity import WikidataItem, WikidataLexeme, WikidataProperty
from qwikidata.datavalue import WikibaseEntityId, Time, Quantity, GlobeCoordinate


data_sprql = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"


def get_q(Q):
    Q = Q.replace(
        "https://www.wikidata.org/entity/", "")
    Q = Q.replace(
        "http://www.wikidata.org/entity/", "")
    return Q


WIKIDATA_LDI_URL = "https://www.wikidata.org/wiki/Special:EntityData"


async def aio_get_entity_dict_from_api2(entity_id: typedefs.EntityId, base_url: str = WIKIDATA_LDI_URL, session=None) -> typedefs.EntityDict:
    url = "{}/{}.json".format(base_url, entity_id)
    exc_obj = None
    for i in range(10):
        try:
            async with session.post(url) as response:
                if response.ok:
                    entity_dict_full = await response.json()
                elif response.status == 503:
                    await asyncio.sleep(10*60)
                    continue
                else:
                    continue
            returned_entity_id = next(iter(entity_dict_full["entities"]))
            entity_dict = entity_dict_full["entities"][returned_entity_id]
            return entity_dict
        except:
            await asyncio.sleep(10)
            exc_type, exc_obj, exc_tb = sys.exc_info()
    raise exc_obj


async def __aio_get_entity_dict_from_api(Q, session=None):
    q_dict = await aio_get_entity_dict_from_api2(Q, session=session)
    print(q_dict)
    q_ = WikidataItem(q_dict)
    return q_, q_dict


async def wikidata_linked(Q,  session=None):
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
                except:
                    pass
    return data
