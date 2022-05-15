import socket
from urllib.parse import urljoin
from urllib.request import urlopen
import aiohttp
from bs4 import BeautifulSoup
import urllib
import markdown
from regex import B
from urllib3 import request

from ResourceDiscovery.uitls.robot import Robots
headers = {
    "User-Agent": ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) FeedScaner"),
    "Accept": ("text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"),
    "Accept-Language": ("en-GB,en-US;q=0.9,en;q=0.8"),
    "Connection": ("keep-alive"),
    "Upgrade-Insecure-Requests": ("1"),
    "Sec-Fetch-Dest": ("document"),
    "Sec-Fetch-Mode": ("navigate"),
    "Sec-Fetch-Site": ("cross-site"),
    "Sec-Fetch-User": ("?1"),
    "Pragma": ("no-cache"),
    "Cache-Control": ("no-cache"),
    "TE": ("trailers"),
    "content-length": ("0")
}


# async def website1(url, id=None):
#     exter_cat = {}
#     for i in range(20):
#         try:
#             req = request.Request(url, headers=headers)
#             with urlopen(req) as response:
#                 if response.status == 200:
#                     htext = response.read()
#                     return str(htext), "html", "unknown", exter_cat, [url]
#         except BaseException as e:
#             print(e)
#             pass
#     return None, None, None, exter_cat, [url]


async def website(url, id=None, count=10, rb=None):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(family=socket.AF_INET, verify_ssl=False)) as session:
        exter_cat = {}
        robot = urljoin(url, '/robots.txt')
        if rb is None or rb.url == robot:
            rb = Robots()
            await rb.read(session)
            if rb.disallow_all:
                return None, None, None, exter_cat, [url]
        for i in range(20):
            try:
                async with session.get(url, ssl=False, headers=headers) as response:
                    if response.ok:
                        try:
                            soup = await response.text()
                        except:
                            soup = await response.text('ISO-8859-1')
                        if len(soup) < 1000:
                            break
                        try:
                            soup = BeautifulSoup(soup, 'html.parser')
                            result = soup.find(
                                "meta", attrs={"http-equiv": "Refresh"})
                            if result:
                                wait, text = result["content"].split(";")
                                if text.strip().lower().startswith("url="):
                                    url = text[4:]
                                    if count != 0:
                                        return website(url, id=id, count=count-1)
                            result = soup.find("frameset")
                            if result:
                                # skip on frameset
                                break
                            result = soup.find("frame")
                            if result:
                                # skip on frame
                                break
                            for s in soup.select('frameset'):
                                s.extract()
                            for s in soup.select('script'):
                                s.extract()
                            for s in soup.select('link'):
                                s.extract()
                            for s in soup.select('style'):
                                s.extract()
                            for s in soup.select('html'):
                                if s.has_attr('lang'):
                                    lang = s.html["lang"]
                            for s in soup.select('body'):
                                if s.has_attr('lang'):
                                    lang = s.html["lang"]
                            if soup.has_attr('lang'):
                                lang = soup.html["lang"]
                            else:
                                lang = "unknown"
                        except:
                            pass
                        return str(soup), "html", lang, exter_cat, [url]
            except:
                pass
    return None, None, None, exter_cat, [url]


async def website_bs(url, id=None):
    exter_cat = {}
    try:
        data, mime, lang, exter_cat, url = await website(url)
    except:
        return None, None, None, exter_cat, [url]
    if data is not None:
        soup = BeautifulSoup(data, 'html.parser')
        for link in soup.select('article'):
            return str(link), mime, lang, exter_cat, url
    return data, mime, lang, exter_cat, url


async def website_markdown(url, id=None):
    exter_cat = {}
    try:
        data, mime, lang, exter_cat, url = await website(url)
    except:
        return None, None, None, exter_cat, [url]
    if data is not None:
        return markdown.markdown(data), "markdown", lang, exter_cat, url
    return data, "markdown", lang, exter_cat, url
