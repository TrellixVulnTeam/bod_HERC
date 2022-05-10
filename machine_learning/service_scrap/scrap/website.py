import socket
from urllib.request import urlopen
import aiohttp
from bs4 import BeautifulSoup
import urllib
import markdown
from urllib3 import request
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


async def website(url, id=None):
    exter_cat = {}
    for i in range(20):
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(family=socket.AF_INET, verify_ssl=False)) as session:
                async with session.get(url, ssl=False, headers=headers) as response:
                    if response.status_code == 200:
                        try:
                            soup = await response.text()
                        except:
                            spup = await response.text('ISO-8859-1')
                        try:
                            soup = BeautifulSoup(spup, 'html.parser')
                            for s in soup.select('script'):
                                s.extract()
                            for s in soup.select('link'):
                                s.extract()
                            for s in soup.select('style'):
                                s.extract()
                            if soup.has_attr('some_attribute'):
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
