import random
import re
from urllib.parse import urljoin
from service_scrap.scrap.reddit import reddit_redditwebsite, PushShift_redditwebsite, Mix_redditwebsite
from service_scrap.scrap.feed import feed
from service_scrap.scrap.website import website, website_bs, website_markdown
from service_scrap.data_pull.wikidata import wikidata_extact

from urllib.parse import urljoin
from pymongo import MongoClient
from pathlib import Path
scrape_wheres = {
    "wikidata": wikidata_extact
}
scrape_types = {
    "feed": [feed],
    "website": [website, website_bs, website_markdown],
    "unknown": [website, website_bs, website_markdown],
}
scrape_toplevel = [
    reddit_redditwebsite,
    PushShift_redditwebsite,
    Mix_redditwebsite
]
scrape_P = {

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


def do_toplevel(toplevel):
    return "http://www.bbc.com"
    if len(scrape_toplevel) != 0:
        return random.choice(scrape_toplevel)(toplevel)


def do_someting(p=None, type=None, url=None, id=None):
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
    return d(url, id)


def get_scrape_wheres(type):
    if type in scrape_wheres.keys():
        return scrape_wheres[type]
    return scrape_wheres["wikidata"]


client = MongoClient()
scrap = client.scrap
wikidataDb = scrap.website


def get_related_data(document, path, data_=[]):
    for resource2 in document['points']:
        if Path(path) in Path(resource2["path"]).parents:
            data_ = get_scrape_wheres(
                resource2["where"])(resource2, data=data_)
    url = (urljoin(document["to_url"], path))
    return data_, url


def Getdata():
    while True:
        places = wikidataDb.aggregate([{"$sample": {"size": 1}}])
        for i in places:
            if bool(random.getrandbits(1)):
                resource = random.choice(i['points'])
                data_ = get_scrape_wheres(resource['where'])(resource)
                data_, url = get_related_data(
                    i,  resource['path'], data_)
                data, mime, lang, exter_cat = do_someting(
                    url=url, type=resource['type'])
                yield data_, mime,  data, lang, exter_cat
            else:
                new_url = do_toplevel(i["to_url"])
                document = wikidataDb.find_one({'to_url': new_url})
                if document is None:
                    continue
                data_, url = get_related_data(document, "")
                data, mime, lang, exter_cat = do_someting(
                    url=url, type="website")
                yield data_, mime,  data, lang, exter_cat
