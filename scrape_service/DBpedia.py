from uitls.SPRQL import SPRQL
from qwikidata.entity import WikidataItem, WikidataLexeme, WikidataProperty
from qwikidata.datavalue import WikibaseEntityId,Time,GlobeCoordinate
from qwikidata.linked_data_interface import aio_get_entity_dict_from_api
async def sprql_dbpedia():
    data_sprql = SPRQL(url = "http://dbpedia.org/sparql")



async def wikidata_linked(Q,mps={}):
    outpuy =[]
    q_dict = await aio_get_entity_dict_from_api(Q)
    q_ = WikidataItem(q_dict)
    claim_groups = q_.get_truthy_claim_groups()
    for claim in q_dict["claims"]:
        claims = claim_groups[claim]
        if len(claims) > 0:
            for claim in claims:
                try:
                    if isinstance(claim.mainsnak.datavalue , GlobeCoordinate):
                        value = claim.mainsnak.datavalue.value
                        print("GlobeCoordinate")
                    elif isinstance(claim.mainsnak.datavalue , Time):
                        value = claim.mainsnak.datavalue.value
                        outpuy.append({
                            "type":"time",
                            "property_id":claim.property_id,
                            "value":value['time']
                        })
                        continue
                    elif isinstance(claim.mainsnak.datavalue , WikibaseEntityId):
                        value = claim.mainsnak.datavalue.value
                        outpuy.append({
                            "type":"wikidata_item",
                            "property_id":claim.property_id,
                            "value":value['id']
                        })
                        continue
                    elif claim.property_id in mps.keys():
                        print(claim)
                except:
                    pass
    return outpuy