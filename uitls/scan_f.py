
import os
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

FeedAtomTypes = [
    'application/atom+xml',
    'application/atom',
    'text/atom+xml',
    'text/atom',
]
FeedRssTypes = [
    'application/rss+xml',
    'application/rss',
    'application/xml',
    'text/rss+xml',
    'text/xml',
    'text/rss',
]

feedJsonTypes = [
    'application/feed+json',
    'text/feed+json',
]
HTMLTypes = [
    "application/x-hatom",
    "application/xhtml+xml",
    "application/html",
    "text/html",
    "html",
    "text/html; charset=utf-8",
    "text/html;charset=UTF-8"
]
prems = [
    [{'?feed', 'rss'}],
    [{'?feed', 'rss2'}],
    [{'?feed', 'rdf'}],
    [{'?feed', 'atom'}],
    [{"?alt", "rss"}],
    [{"?service", "rss"}],
    [{"?service", "atom"}],
]
feedpaths = [
    "atom.xml",
    "index.atom",
    "index.rdf",
    "rss.xml",
    "index.xml",
    "index.rss",
    "index.json",
    'feed/',
    'feed/rss/',
    'feed/rss2/',
    'feed/rdf/',
    'feed/atom/',
    'services/rss/',
    "rss.xml",
    "feed.xml",
    "rss",
    "atom",
    "feed",
    "newsfeed",
    "rss-feed",
    "rss.jsp",
    "index.xml",
    'news/?feed=rss',
    'news/?feed=rss2',
    'news/?feed=rdf',
    'news/?feed=atom',
    'news/feed/',
    'news/feed/rss/',
    'news/feed/rss2/',
    'news/feed/rdf/',
    'news/feed/atom/',
    'news/services/rss/',
    "news/rss.xml",
    "news/feed.xml",
    "news/rss.php",
    "news/feed.php",
    "news/rss",
    "news/fv",
    "news/atom",
    "news/index.xml",
    "news/newsfeed",
    "news/rss-feed",
]

feedpaths = [
    "atom.xml",
    "index.atom",
    "index.rdf",
    "rss.xml",
    "index.xml",
    "index.rss",
    "index.json",
    'feed/',
    'feed/rss/',
    'feed/rss2/',
    'feed/rdf/',
    'feed/atom/',
    'services/rss/',
    "rss.xml",
    "feed.xml",
    "rss",
    "atom",
    "feed",
    "newsfeed",
    "rss-feed",
    "rss.jsp",
    "index.xml",
    'news/?feed=rss',
    'news/?feed=rss2',
    'news/?feed=rdf',
    'news/?feed=atom',
    'news/feed/',
    'news/feed/rss/',
    'news/feed/rss2/',
    'news/feed/rdf/',
    'news/feed/atom/',
    'news/services/rss/',
    "news/rss.xml",
    "news/feed.xml",
    "news/rss.php",
    "news/feed.php",
    "news/rss",
    "news/fv",
    "news/atom",
    "news/index.xml",
    "news/newsfeed",
    "news/rss-feed",
]


def feed_search_cms(soup, url):
    links = []
    for feedpath in feedpaths:
        links.append(urljoin(url, feedpath))
        links.append(urljoin(url, "/" + feedpath))
    return links


def feed_search_links(soup, url):
        url = str(url)
        links = []
        link_tags = soup.find_all("link")
        for link in link_tags:
            if link.has_attr('href') and link.has_attr('type'):
                if link.get("type") in "rss":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                elif link.get("type") in "atom":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                elif link.get("type") in "json":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                elif link.get("rel") in "alternate":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                elif link.get("rel") in "self":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
            elif link.has_attr('href'):
                o = urlparse(link["href"])
                if "rss" in o.path:
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                elif "atom" in o.path:
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                elif "json" in o.path:
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                ext = os.path.splitext(o.path)[1]
                if ext == ".xml":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                if ext == ".json":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                if ext == ".xhtml":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                if ext == ".rss":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                if ext == ".atom":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                elif link.get("rel") in "self":
                    last_a_tag = soup.find("a", rel="hub")
                    if last_a_tag is not None:
                        if link.get("href"):
                            links.append({"type":"feed","href":urljoin(url, link["href"]),"self":urljoin(url,  last_a_tag["href"])})
        link_tags = soup.find_all("a")
        for link in link_tags:
            if link.has_attr('href') and link.has_attr('type'):
                if link.get("type") in "rss":
                    links.append({"type":"feed","href":urljoin(url, link["href"])})
                elif link.get("type") in "atom":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                elif link.get("type") in "json":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
                elif link.get("rel") in "self":
                    links.append({"type":"feed","href":urljoin(url,  link["href"])})
            elif link.has_attr('href'):
                    o = urlparse(link["href"])
                    if "rss" in o.path:
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    elif "atom" in o.path:
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    elif "json" in o.path:
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    ext = os.path.splitext(o.path)[1].lower()
                    if ext == ".xml":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".json":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".xhtml":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".rss":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".atom":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    elif link.get("rel") in "self":
                        last_a_tag = soup.find("a", rel="hub")
                        if last_a_tag is not None:
                            if link.get("href"):
                                links.append({"type":"feed","href":urljoin(url, link["href"]),"self":urljoin(url,  last_a_tag["href"])})
        link_tags = soup.find_all("area")
        if link.has_attr('href') and link.has_attr('type'):
            for link in link_tags:
                if link.get("type") in "rss":
                    links.append(urljoin(url,  link["href"]))
                elif link.get("type") in "atom":
                    links.append(urljoin(url,  link["href"]))
                elif link.get("type") in "json":
                    links.append(urljoin(url, link["href"]))
                elif link.get("rel") in "self":
                    last_a_tag = soup.find("a", rel="hub")
                    if last_a_tag is not None:
                        if link.get("href"):
                            links.append({"type":"feed","href":urljoin(url, link["href"]),"self":urljoin(url,  last_a_tag["href"])})
        elif link.has_attr('href'):
                    o = urlparse(link["href"])
                    if "rss" in o.path:
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    elif "atom" in o.path:
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    elif "json" in o.path:
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    ext = os.path.splitext(o.path)[1].lower()
                    if ext == ".xml":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".json":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".xhtml":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".rss":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".atom":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
        elif link.has_attr('href'):
                    o = urlparse(link["href"])
                    if "rss" in o.path:
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    elif "atom" in o.path:
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    elif "json" in o.path:
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    ext = os.path.splitext(o.path)[1].lower()
                    if ext == ".xml":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".json":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".xhtml":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".rss":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
                    if ext == ".atom":
                        links.append({"type":"feed","href":urljoin(url,  link["href"])})
        return links




async def scanHTML(text, url_):
    calls = []
    feeds = []
    isGood = False
    
    try:
        soup = BeautifulSoup(text, 'html.parser')
        feeds =+ feed_search_cms(soup,url_)
        feeds =+ feed_search_links(soup,url_)
        feeds =+ scanHTML(soup,url_)
        isGood = True
    except:
        isGood = False
    for feed in feeds:
        if feed["type"] == "feed":
            calls.append(feed_do(feed))
        if feed["type"] == "self":
            calls.append(websub_do(feed))
    return isGood, feeds