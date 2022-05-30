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
#             
#             pass
#     return None, None, None, exter_cat, [url]

def recursiveChildren(x):
    a = {}
    for child in x.childGenerator():
        has_property =child.has_attr("property")
        has_rel =child.has_attr("rel")
        has_rev =child.has_attr("rev")
        has_resource =child.has_attr("resource")
        has_href =child.has_attr("href")
        has_content =child.has_attr("content")
        has_datatype =child.has_attr("datatype")
        has_about =child.has_attr("about")
        has_typeof =child.has_attr("typeof")
        has_class =child.has_attr("class")
        has_src =child.has_attr("src")
        has_type =child.has_attr("type")
        has_typeof =child.has_attr("typeof")
        has_vocab =child.has_attr("vocab")
        has_src =child.has_attr("src")
        # RDFa
        if has_property and has_content and has_typeof:
            data =recursiveChildren(child)
            
            pass
        elif has_typeof and has_vocab:
            recursiveChildren(child)
            pass
        elif has_property and has_content:
            data =recursiveChildren(child)
            pass
        elif has_property and has_rel and has_datatype:
            data =recursiveChildren(child)
            pass
        elif has_property and has_rev and has_datatype:
            data =recursiveChildren(child)
            pass
        elif has_property and has_href and has_datatype:
            data =recursiveChildren(child)
            property =child.get('property')
            print(property)
            href =child.get('href')
            datatype =child.get('datatype')
            pass
        elif has_property and has_resource and has_datatype:
            property =child.get('property')
            print(property)
            resource =child.get('resource')
            datatype =child.get('datatype')
            data =recursiveChildren(child)
            pass
        elif has_property and has_src and has_datatype:
            property =child.get('property')
            src =child.get('src')
            datatype =child.get('datatype')
            data =recursiveChildren(child)
            pass
        elif has_property and has_rel:
            data =recursiveChildren(child)
            rel =child.get('rel')
            property =child.get('property')
            pass
        elif has_property and has_rev:
            data =recursiveChildren(child)
            rev =child.get('rev')
            property =child.get('property')
            print(property)
            pass
        elif has_property and has_href:
            data =recursiveChildren(child)
            href =child.get('href')
            property =child.get('property')
            print(property)
            pass
        elif has_property and has_resource:
            data =recursiveChildren(child)
            resource =child.get('resource')
            property =child.get('property')
            print(property)
            pass
        elif has_property and has_src:
            data =recursiveChildren(child)
            resource =child.get('resource')
            property =child.get('property')
            print(property)
            src =child.get('src')
            pass
        elif has_property and has_datatype:
            data =recursiveChildren(child)
            pass
        elif has_vocab and has_datatype:
            data =recursiveChildren(child)
            pass
        elif has_property:
            property =child.get('property')
            print(property)
            data =recursiveChildren(child)
            pass
        elif has_about:
            data =recursiveChildren(child)
            pass
        elif has_typeof:
            data =recursiveChildren(child)
            pass
        elif has_vocab:
            data =recursiveChildren(child)
            pass
        #  
        elif has_class and has_content:
            pass
        elif has_class:
            pass
        if has_type and has_src:
            pass
    # json-dl
    return a




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
                            recursiveChildren(soup)
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
