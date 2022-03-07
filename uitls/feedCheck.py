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
        return False, []
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


def feedCheck(contex):
    check, urls = feedCheck_JSON_Feed(contex)
    if check:
        return check
    check, urls = feedCheck_ATOM(contex)
    if check:
        return check
    check, urls = feedCheck_RSS(contex)
    if check:
        return check
    return False