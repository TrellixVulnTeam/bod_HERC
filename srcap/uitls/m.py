import os
from urllib.parse import urlparse
from uitls.web_wehsite import url_add2
import re
url_reg_callbacks = []
mime_callbacks = []
wikidataP_callbacks = []
init_callbacks = []
tick_callbacks = []


def load():
    for i_dir in os.listdir("./service"):
        pass


def add_tick_callbacks(callback):
    tick_callbacks.append((callback))


def add_init_callbacks(callback):
    init_callbacks.append((callback))


def add_wikidataP_callback(mime, callback):
    wikidataP_callbacks.append((mime, callback))


def add_mime_callback(mime, callback):
    mime_callbacks.append((mime, callback))


def add_urlReg_callback(reg, callback):
    url_reg_callbacks.append((reg, callback))


async def do_url(url, mime, status, where, session):
    block = False
    for mime_callback in mime_callbacks:
        if mime_callback[0] in mime:
            block = block | await mime_callback[1](mime_callback, url, mime, status)
    for urlReg_callback in url_reg_callbacks:
        match = re.match(urlReg_callback[0], url)
        if match:
            block = block | await urlReg_callback[1](urlReg_callback, url, mime, status)
    if block:
        return
    if status != "200" and status != "" and status is not None:
        return
    if mime == "xml":
        await url_add2(url, where, item_type="feed", session=session)
    elif mime == "atom":
        await url_add2(url, where, item_type="feed", session=session)
    elif mime == "rss":
        await url_add2(url, where, item_type="feed", session=session)
    elif mime == "json":
        await url_add2(url, where, item_type="feed", session=session)
    elif mime == "html":
        o = urlparse(url)
        url = o.scheme+"://"+o.netloc
        await url_add2(url, where, item_type="website", session=session)
