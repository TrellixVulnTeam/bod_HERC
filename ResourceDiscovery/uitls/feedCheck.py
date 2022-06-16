import json
import os
import re
import sys


def feedCheck_RSS(text,encoding):
    feed = []
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(text, 'xml')
        rss = soup.find('rss')
        if rss is not None:
            for item in soup.findAll('item'):
                for link in soup.findAll('link'):
                    feed.append(link.get_text())
            return True, feed
    except:
        return False, []
    return False, feed


def feedCheck_ATOM(text,encoding):
    feed = []
    c = False
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(text, 'xml')
        feed_ = soup.find('feed')
        if feed_ is not None:
            for link in soup.findAll('link'):
                if link.has_attr('href'):
                    feed.append(link["href"])
            for entry in soup.findAll('entry'):
                c = True
        return c, feed
    except:
        return False, []
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
            return False, []
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
        return False, feed
    return False, feed


size_max = 0
def feedCheck(text,mime,encoding):
    print("mine:",mime)
    global size_max
    if "html" in mime:
        return False, []
    if "image" in mime:
        return False, []
    if "gzip" in mime:
        return False, []
    if "audio" in mime:
        return False, []
    if "font" in mime:
        return False, []
    if "video" in mime:
        return False, []
    if  mime is not None and mime != "":
        print("feed Mime:",mime)
    if mime is  None:
        mime =""
    try:
        if "atom" in mime:
            check, urls = feedCheck_ATOM(text,encoding)
            if check and len(urls) != 0:
                
                return check, urls
        if "rss" in mime:
            check, urls = feedCheck_RSS(text,encoding)
            if check and len(urls) != 0:
                
                return check, urls
        elif "atom" in mime or "xml" in mime:
            check, urls = feedCheck_RSS(text,encoding)
            if check and len(urls) != 0:
                
                return check, urls
            check, urls = feedCheck_ATOM(text,encoding)
            if check and len(urls) != 0:
                
                return check, urls
            return False, []
        # elif (re.match(r'^([\{\[](\n|.)*[\]\}])$', data)) or "json" in mime:
        #   del text
        #   del data
        #   check, urls = feedCheck_JSON_Feed(contex)
        #   if check and len(urls) != 0:
            # return check, urls
        else:
            check, urls = feedCheck_RSS(text,encoding)
            if check and len(urls) != 0:
                size_max = max(len(text),size_max)
                return check, urls
            check, urls = feedCheck_ATOM(text,encoding)
            if check and len(urls) != 0:
                size_max = max(len(text),size_max)
                return check, urls
    except:    
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("G",exc_type, exc_obj, exc_tb,fname,exc_tb.tb_lineno)
    return False, []
