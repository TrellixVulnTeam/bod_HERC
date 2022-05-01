
import re

from regex import F


url_mach_lookup = {}
url_mach_callback = {}
P_callback = {}
Q_callback = []

def add_P_mach_url(url, P):
    if url not in url_mach_lookup.keys():
        url_mach_lookup[url] = []
    url_mach_lookup[url].append(P)


def add_p_callback(p, callback):
    if p not in P_callback.keys():
        P_callback[p] = []
    P_callback[p].append(callback)


def add_mach_url_callback(url, callback):
    url_mach_callback[url] = callback
    for pattern in url_mach_lookup.keys():
        cc = re.match(pattern, url)
        if cc:
            do_callback_P(url, cc[1])


def do_callback_Q(id, data=None):
    for callback in Q_callback:
        return callback(id, data)


def do_callback_P(p, id, data=None):
    if p not in P_callback.keys():
        return False
    for callback in P_callback[p]:
        return callback(id, data)


def do_callback_url_mach(url, data=None):
    for i in url_mach_lookup.keys():
        check = re.match(i, url)
        if check:
            for p in url_mach_lookup[url]:
                do_callback_P(p, check[1], data)
            break
    for i in url_mach_callback.keys():
        check = re.match(i, url)
        if check:
            url_mach_callback[i](url, check[1], data)
            break


def test_url_mach(url):
    for i in url_mach_lookup.keys():
        check = re.match(i, url)
        if check:
            return True, url_mach_lookup[i]
    return False , None
