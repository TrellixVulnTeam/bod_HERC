def wikidata_extact(resource, data={}):
    if "data" in resource.keys():
        if "item" in resource["data"].keys():
            if "wikidata_item" not in data.keys():
                data["wikidata_item"] = []
            data["wikidata_item"].append(resource["data"]["item"])
            if resource["data"]["item"]not in data["wikidata_item"]:
                data["wikidata_item"].append(resource["data"]["item"])
        if "prop" in resource["data"].keys():
            if "wikidata_prop" not in data.keys():
                data["wikidata_prop"] = []
            if resource["data"]["prop"]not in data["wikidata_prop"]:
                data["wikidata_prop"].append(resource["data"]["prop"])
        if "data" in resource["data"].keys():
            for i_resource in resource["data"]["data"]:
                key_data = ("wikidata_"+list(i_resource.keys())[0])
                key_resource = (list(i_resource.keys())[0])
                if i_resource[key_resource][0] != "Q" and i_resource[key_resource][0] != "P":
                    continue
                if key_data not in data.keys():
                    data[key_data] = []
                if i_resource[key_resource] not in data[key_data]:
                    data[key_data].append(i_resource[key_resource])
    return data
