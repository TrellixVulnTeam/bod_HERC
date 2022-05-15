async def wikidata_extact2(resource, data={}):
    if "prop" in resource.keys():
        if "wikidata_prop" not in data.keys():
            data["wikidata_prop"] = []
        if resource["prop"] not in data["wikidata_prop"]:
            data["wikidata_prop"].append(resource["prop"])

    if "item" in resource.keys():
        if "wikidata_item" not in data.keys():
            data["wikidata_item"] = []
        if resource["item"] not in data["wikidata_item"]:
            data["wikidata_item"].append(resource["item"])

    if "value" in resource.keys():
        if "wikidata_value" not in data.keys():
            data["wikidata_value"] = []
        if resource["value"] not in data["wikidata_value"]:
            data["wikidata_value"].append(resource["value"])

    if "data" in resource.keys() and resource["data"] is not None:
        for i_resource in resource["data"]:
            key_data = ("wikidata_"+list(i_resource.keys())[0])
            key_resource = (list(i_resource.keys())[0])
            if i_resource[key_resource][0] != "Q" and i_resource[key_resource][0] != "P":
                continue
            if key_data not in data.keys():
                data[key_data] = []
            if i_resource[key_resource] not in data[key_data]:
                data[key_data].append(i_resource[key_resource])
    return data


# def wikidata_extact(resource, data={}):
#     print("resource", resource.keys())
#     if "data" in resource.keys():
#         if "item" in resource.keys():
#             if "wikidata_item" not in data.keys():
#                 data["wikidata_item"] = []
#             if resource["item"]not in data["wikidata_item"]:
#                 data["wikidata_item"].append(resource["item"])
#         if "prop" in resource.keys():
#             if "wikidata_prop" not in data.keys():
#                 data["wikidata_prop"] = []
#             if resource["prop"]not in data["wikidata_prop"]:
#                 data["wikidata_prop"].append(resource["prop"])
#         if "data" in resource.keys():
#             for i_resource in resource["data"]:
#                 key_data = ("wikidata_"+list(i_resource.keys())[0])
#                 key_resource = (list(i_resource.keys())[0])
#                 if i_resource[key_resource][0] != "Q" and i_resource[key_resource][0] != "P":
#                     continue
#                 if key_data not in data.keys():
#                     data[key_data] = []
#                 if i_resource[key_resource] not in data[key_data]:
#                     data[key_data].append(i_resource[key_resource])
#     return data
