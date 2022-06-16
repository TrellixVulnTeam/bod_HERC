import json
import os
import random
import sys
import requests
from machine_learning.service_scrap.scrap.website import website_bs, website_markdown
from machine_learning.service_scrap.scrap.website import website
c = [website, website_bs, website_markdown]


def feedCheck_RSS(contex):
    feed = []
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(contex, 'xml')
        rss = soup.find('rss')
        if rss is not None:
            for item in soup.findAll('item'):
                for link in soup.findAll('link'):
                    feed.append(link.get_text())
            return True, feed
    except:
        return False, feed
    return False, feed


def feedCheck_ATOM(contex):
    feed = []
    c = False
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(contex, 'xml')
        feed_ = soup.find('feed')
        if feed_ is not None:
            for link in soup.findAll('link'):
                if link.has_attr('href'):
                    feed.append(link["href"])
            for entry in soup.findAll('entry'):
                c = True
        return c, feed
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("G",exc_type, exc_obj, exc_tb,fname,exc_tb.tb_lineno)
        return False, feed
    return False, feed


def feedCheck_JSON_Feed(contex):
    feed = []
    try:
        data = json.loads(contex)
        if "https://jsonfeed.org" in data["version"]:
            pass
        elif "https://jsonfeed.org" in data["version"]:
            pass
        else:
            return False
        if "home_page_url" in data.keys():
            feed.append(data["home_page_url"])
        if "items" in data.keys():
            if len(data["items"]) > 0:
                for i in data["items"]:
                    if "url" in i:
                        feed.append(i["url"])
                    if "external_url" in i:
                        feed.append(i["external_url"])
                    pass
                return True, feed
        else:
            return False, feed
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("G",exc_type, exc_obj, exc_tb,fname,exc_tb.tb_lineno)
        return False, feed
    return False, feed

async def feed(url, id):
    exter_cat = {}
    data = await website(url)
    check, feed = feedCheck_RSS(data)
    data = None
    if check:
        if len(feed) != 0:
            feed = random.choice(feed)
            data, mime, lang, exter_cat, url2 = random.choice(c)(feed)
            return data, mime, lang, exter_cat, [url, url2]
    check, feed = feedCheck_ATOM(data)
    if check:
        if len(feed) != 0:
            feed = random.choice(feed)
            data, mime, lang, exter_cat, url2 = random.choice(c)(feed)
            return data, mime, lang, exter_cat, [url, url2]
    check, feed = feedCheck_JSON_Feed(data)
    if check:
        if len(feed) != 0:
            feed = random.choice(feed)
            data, mime, lang, exter_cat, url2 = random.choice(c)(feed)
            return data, mime, lang, exter_cat, [url, url2]

    return None, None, None, exter_cat, [url]
