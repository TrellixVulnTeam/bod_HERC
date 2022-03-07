import asyncio
import json
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from validators import validator
from requests import PreparedRequest
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


async def scanHTML(text, url_):
    subhub = []
    feed = []
    isGood = False
    
    async def feed_do(url):
        await url_feed(url, where="internal")
    try:
        soup = BeautifulSoup(text, 'html.parser')
        # Scan for LINKS
        for i in soup.select('a'):
            if i.has_attr('href'):
                if i.has_attr('type'):
                    for type in ["rss", "xml", "atom",  "json"]:
                        if type in link["type"]:
                            feed.append(feed_do(link["href"]))
                            continue
                if ["rss", "rdf", "json", "xml", "atom", "feed", "json"] in link["href"].lower():
                    feed.append(feed_do(link["href"]))
                    continue
            if not link.has_attr('rel'):
                continue
            else:
                if "alternate" in link["rel"]:
                    feed.append(feed_do(link["href"]))
                    continue

        for i in soup.select('link'):
            if i.has_attr('href'):
                if i.has_attr('type'):
                    for type in ["rss", "xml", "atom",  "json"]:
                        if type in link["type"]:
                            feed.append(feed_do(link["href"]))
                            continue
                if ["rss", "rdf", "json", "xml", "atom", "feed", "json"] in link["href"].lower():
                    feed.append(feed_do(link["href"]))
                    continue
            if not i.has_attr('rel'):
                feed.append(feed_do(link["href"]))
                continue
            if "alternate" in link["rel"]:
                feed.append(feed_do(link["href"]))
                continue
        for link in soup.select('area'):
            if link.has_attr('href'):
                if link.has_attr('type'):
                    for type in ["rss", "xml", "atom",  "json"]:
                        if type in link["type"]:
                            feed.append(feed_do(link["href"]))
                            continue
                if ["rss", "rdf", "json", "xml", "atom", "feed", "json"] in link["href"].lower():
                    feed.append(feed_do(link["href"]))
                    continue
            if not link.has_attr('rel'):
                continue
            else:
                if "alternate" in link["rel"]:
                    feed.append(feed_do(link["href"]))
                    continue
    except:
        pass
    for prem in prems:
        req_page = PreparedRequest()
        req_page.prepare_url(url_, prem)
    for feedpath in feedpaths:
        feed.append(feed_do(urljoin(url_, "/"+feedpath)))
    for feedpath in feedpaths:
        feed.append(feed_do(urljoin(url_, feedpath)))
    all_groups = await asyncio.gather(*feed)
    return isGood, subhub, feed