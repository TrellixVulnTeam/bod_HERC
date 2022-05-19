import json
import aiohttp
import asyncio
import random
import ResourceDiscovery.alt_savices.toplevel as toplevel
mime_filter = [
    "html",
    "rss",
    "json",
]
mime_fliter_ = ["mime-detected", "mime"]
url_json = "https://index.commoncrawl.org/collinfo.json"


async def URL_GEN():
    async with aiohttp.ClientSession() as client:
        async with client.get(url_json) as response:
            data = await response.json()
            index = random.randrange(len(data))
            return data[index]["cdx-api"]


async def get_some_CC():
    seen_url = set()
    good = False
    while True:
        url = await URL_GEN()
        for i in range(5):
            mime = random.choice(mime_filter)
            mime = random.choice(mime_filter)
            fliter_m = random.choice(mime_fliter_)
            top = random.choice(toplevel.toplevels)
            queryNumPages = [
                ("output", "json"),
                ("fl", "url"),
                ("filter", "status:200"),
                ("filter", fliter_m+":"+mime),
                ("url", "*"+top),
                ("showNumPages", "true"),
            ]

            async with aiohttp.ClientSession() as client:
                for i in range(20):
                    async with client.get(url, params=queryNumPages) as response:
                        if response.ok:
                            data = await response.text()
                            data = json.loads(data)
                            good = True
                            break
                        else:
                            print("wait for 20 & status:",
                                  response.status, " & url: ", url)
                            await asyncio.sleep(20)
                if not good:
                    continue
                if data["pages"] != 0:
                    page_index = random.randrange(int(data["pages"]))
                else:
                    page_index = 0
                query = [
                    ("fields", "url,mime,mime-detected,status"),
                    ("output", "json"),
                    ("filter", "status:200"),
                    ("filter", fliter_m+":"+mime),
                    ("url", "*"+top),
                    ("page", str(page_index)),
                ]
                good = False
                for i in range(20):
                    async with client.get(url, params=query) as response:
                        if response.ok:
                            text = await response.text()
                            for newline in text.split("\n"):
                                try:
                                    data = json.loads(newline)
                                    if data["url"] in seen_url:
                                        print("i know this one[")
                                        continue
                                    else:
                                        print("cat")
                                    seen_url.add(data["url"])
                                    yield data
                                    good = True
                                except:
                                    print("error", text)
                            if good:
                                break
                        elif response.status == 404:
                            break
                        else:
                            print("wait for 20 & status:",
                                  response.status, " & url: ", url)
                            await asyncio.sleep(20)
                    if good:
                        break
        if good:
            break
