import os
import socket
from urllib.parse import urljoin
from urllib.request import urlopen
import aiohttp
from bs4 import BeautifulSoup ,Comment ,NavigableString
import urllib
import markdown
from regex import B, P
from urllib3 import request
import sys
import re
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
rel_skip = [
"alternate",
"author",
"bookmark",
"canonical",
"dns-prefetch",
"external",
"help",
"icon",
"license",
"manifest",
"me",
"modulepreload",
"next",
"nofollow",
"noopener",
"noreferrer",
"opener",
"pingback",
"preconnect",
"prefetch",
"preload",
"prerender",
"prev",
"search",
"stylesheet",
"tag",
"shortlink",
"wlwmanifest",
"home",
"apple-touch-icon",
"shortlink",
"category",
"mask-icon",
"profile",
"EditURI",
"Shortcut",
"Icon",
"https://api.w.org/"
]



def semantic_website_passer(x,url = "" ,i=0):
    context = {}
    graph = {}
    ix = 0
    for child in x.children:
        try:
            ix = ix +1
            name = child.name
            if isinstance(child, Comment):
                continue
            if isinstance(child, NavigableString):
                continue
            if isinstance(name, type(None)):
                print(type(child))
                data = {**data,** semantic_website_passer(child,i+1)}
                continue
            is_base = name == "base"
            has_vocab = child.has_attr("vocab")  and (child.get("vocab") != "")
            has_rel = child.has_attr("rel")  and (child.get("rel") != "")
            has_rev = child.has_attr("rev")  and (child.get("rev") != "")
            has_src = child.has_attr("src")  and (child.get("src") != "")
            has_href = child.has_attr("href")  and (child.get("href") != "")
            has_resource = child.has_attr("resource") and (child.get("resource") != "")
            has_property = child.has_attr("property") and (child.get("property") != "")
            has_content = child.has_attr("content") and (child.get("content") != "")
            has_datatype = child.has_attr("datatype") and (child.get("datatype") != "")
            has_prefix = child.has_attr("prefix") and (child.get("prefix") != "")
            has_typeof = child.has_attr("typeof") and (child.get("typeof") != "")
            has_about = child.has_attr("about")  and (child.get("about") != "")
            has_class = child.has_attr("class") and (child.get("class") != "")
            
            if has_rel and has_href and has_typeof:
                child.get("rel")
                child.get("href")
                child.get("typeof")
            elif has_rev and has_href  and has_typeof:
                print("rev and href and typeof")
            elif has_rev and has_src  and has_typeof:
                print("rev and src and typeof")
            elif has_rel and has_src and has_typeof:
                print("rel and src and typeof")
            elif has_rev and has_resource and has_typeof:
                print("rev and resource and typeof")
            elif has_rel and has_resource and has_typeof:
                print("rel and resource and typeof")
            elif has_rel and has_href:
                rel =(child.get("rel"))
                href =(child.get("href"))
                S = False
                for i_rel in rel:
                    if i_rel in rel_skip:
                        S = True
                        break
                if S:
                    continue
                context2 ,graph2 = semantic_website_passer(child,i+1)
                graph = {**graph,** graph2}
                context = {**context,** context2}
            elif has_rev and has_href:
                print("rev and href")
            elif has_rev and has_src:
                print("rev and src")
            elif has_rel and has_src:
                print("rel and src")
            elif has_rev and has_resource:
                print("rev and resource")
            elif has_rel and has_resource:
                print("rel and resource")
            elif has_rev and has_property:
                print("rev and property")
            elif has_rel and has_property:
                print("rel and property")
            elif has_property and has_about:
                print("property and about")
            elif has_property and has_datatype:
                print("property and datatype")
            elif has_property and has_content:
                graph[child.get("property")]=child.get("content")
            elif has_property and has_typeof:
                print("property and typeof")
            elif has_vocab and has_typeof:
                context[child.get("typeof")] = urljoin(child.get("vocab"),child.get("typeof"))
                context2 ,graph2 = semantic_website_passer(child,i+1)
                graph = {**graph,** graph2}
                context = {**context,** context2}
            # elif is_base and has_href:
            #     print("base and href")
            
            elif has_property and has_href:
                graph[child.get("property")]=child.get("href")
            elif has_about:
                print("property")
            elif has_prefix:
                prefix = child.get("prefix")
                for m in re.finditer(r"([A-z]*): (https?:\/\/[\/a-zA-Z0-9@:%&._\+~?#=&]*)", prefix):
                    context[m.group(1)] = m.group(2)
            elif has_vocab:
                print("vocab:",child.get("vocab"))
                context2 ,graph2 = semantic_website_passer(child,i+1)
                graph = {**graph,** graph2}
                context = {**context,** context2}
                pass
            elif has_class:
                context2 ,graph2 = semantic_website_passer(child,i+1)
                graph = {**graph,** graph2}
                context = {**context,** context2}
                pass
                # print("class")
            else:
                context2 ,graph2 = semantic_website_passer(child,i+1)
                graph = {**graph,** graph2}
                context = {**context,** context2}
        except BaseException as e :
            print(e)
            pass
        except:
            print("e")
    # if i == 0:
    #     pass
    #     if len(graph.keys()) != 0 or len(context.keys()) != 0:
    #         print("url:",url)
    #     if len(graph.keys()) != 0:
    #         print("graph:",graph)
    #     if len(context.keys()) != 0:
    #         print("context:",context)
    return context ,graph




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
                            soup = BeautifulSoup(soup, 'html5lib')
                            semantic_website_passer(soup,url=response.url)
                            result = soup.find(
                                "meta", attrs={"http-equiv": "Refresh"})
                            if result:
                                wait, text = result["content"].split(";")
                                if text.strip().lower().startswith("url="):
                                    url_new = text[4:]
                                    if count != 0:
                                        return website(url_new, id=id, count=count-1)
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
