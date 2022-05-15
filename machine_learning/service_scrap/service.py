import os
import random
import re
import sys
from urllib.parse import urljoin, urlparse
from machine_learning.service_scrap.scrap.reddit import reddit_redditwebsite, PushShift_redditwebsite, Mix_redditwebsite
from machine_learning.service_scrap.scrap.feed import feed
from machine_learning.service_scrap.scrap.website import website,  website_bs, website_markdown
from machine_learning.service_scrap.data_pull.wikidata import wikidata_extact2

from urllib.parse import urljoin
from pymongo import MongoClient
from pathlib import Path
scrape_wheres = {
    "wikidata": wikidata_extact2
}
scrape_types = {
    "feed": [feed],
    "website": [website],
    "unknown": [website],
}
scrape_toplevel = [
    reddit_redditwebsite,
    # PushShift_redditwebsite,
    # Mix_redditwebsite
]
scrape_P = {

}
scrape_Q = {

}
scrape_url_format = {

}
scrape_file_format = {

}
scrape_mime_format = {

}
image_format = ["jpg", "jpeg", "jpe", "jif", "jfif", "jfi", "jp2", "j2k", "jpf", "jpm", "jpg2", "j2c", "jpc", "jpx", "mj2", "jpg", "tif",
                "wav", "png", "webp", "tiff", "tif", "gif", "bmp", "dib", "png", "webp", "heif", "heifs", "heic", "heics", "avci", "avcs", "avif", "avifs"]
video_format = ["webm", "mkv", "flv", "flv", "vob", "ogv,", "ogg", "drc", "gif", "gifv", "mng", "avi", "mts,", "m2ts,", "ts", "mov,", "qt", "wmv", "yuv", "rm", "rmvb",
                "viv", "asf", "amv", "mp4,", "m4p", "m4v", "mpg, ", "mp2, ", "mpeg, ", "mpe, ", "mpv", "mpg, ", "mpeg, ", "m2v", "m4v", "svi", "3gp", "3g2", "mxf", "roq", "nsv", "flv",
                "f4v", "f4p", "f4a", "f4b"]


async def do_toplevel(toplevel):
    a = random.choice(scrape_toplevel)
    return await a(toplevel)

# prop
# value
# item


async def do_someting2(resource, url=None):
    thngs_i_could_do = []
    if "prop" in resource.keys():
        if resource["prop"] in scrape_P.keys():
            thngs_i_could_do = thngs_i_could_do + scrape_P[resource["prop"]]
    if "item" in resource.keys():
        if resource["item"] in scrape_Q.keys():
            thngs_i_could_do = thngs_i_could_do + scrape_Q[resource["item"]]
    if "type" in resource.keys():
        if resource["type"] in scrape_types.keys():
            thngs_i_could_do = thngs_i_could_do + \
                scrape_types[resource["type"]]
    if len(thngs_i_could_do) == 0:
        return None, None, None, {}, []
    else:
        d = random.choice(thngs_i_could_do)
        b = d(url, resource)
        c = await b
        return c


async def do_someting(p=None, type=None, url=None, id=None):
    thngs_i_could_do = []
    if p is not None:
        if p in scrape_P.keys():
            thngs_i_could_do = thngs_i_could_do + scrape_P[p]
    if url is not None:
        for url_i in scrape_url_format.keys():
            m = re.search(url_i, url)
            if m:
                thngs_i_could_do = thngs_i_could_do + scrape_url_format[url_i]
                id = m.group(1)
    if type is not None:
        if type in scrape_types.keys():
            thngs_i_could_do = thngs_i_could_do + scrape_types[type]
    if len(thngs_i_could_do) == 0:
        return None
    d = random.choice(thngs_i_could_do)
    return await d(url, id)


client = MongoClient()
scrap = client.scrap
wikidataDb = scrap.website


# def get_related_data(document, path, data_=[]):
#     for resource2 in document['points']:
#         if Path(path) in Path(resource2["path"]).parents:
#             data_ = get_scrape_wheres(
#                 resource2["where"])(resource2, data=data_)
#     url = (urljoin(document["to_url"], path))
#     return data_, url


async def get_class_data(document, path, data_={}):
    for resource2 in document['points']:
        if Path(path) in Path(resource2["path"]).parents or path == resource2["path"]:
            data_c = scrape_wheres[resource2["where"]]
            data_ = await data_c(resource2, data=data_)
    return data_


async def Getdata():
    while True:
        try:
            places = wikidataDb.aggregate([{"$sample": {"size": 1}}])
        except:
            continue
        for i_doc in places:
            if bool(random.getrandbits(1)):
                resource = random.choice(i_doc['points'])
                if "path" in resource.keys():
                    url = urljoin(i_doc["to_url"], resource["path"])
                else:
                    url = None
                a2 = await do_someting2(resource, url)
                # print(a2)
                data, mime, lang, data_, url2 = a2
                if data is None:
                    continue
                data_ = await get_class_data(i_doc, resource["path"], data_=data_)
                o = urlparse(url)
                url = o.scheme + "://" + o.netloc
                for url in url2:
                    data_ = await get_class_data(i_doc, o.path, data_=data_)

                yield data_, mime,  data, lang
            else:
                data, mime, lang, data_, urls = await do_toplevel(i_doc["to_url"])
                if data is None:
                    continue
                for url in urls:
                    try:
                        o = urlparse(url)
                        url = o.scheme + "://" + o.netloc
                        document = wikidataDb.find_one({'to_url': url})
                        if document is not None:
                            data_ = await get_class_data(
                                document, o.path, data_=data_)
                    except:
                        pass
                data_ = await get_class_data(i_doc, o.path, data_=data_)
                yield data_, mime,  data, lang
