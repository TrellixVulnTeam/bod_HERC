import json
from habanero import Crossref
import enlighten
cr = Crossref()
manager = enlighten.get_manager()
offset = 0
pbar = manager.counter(total=0, desc='Initializing:', unit='initials')
while True:
    res = cr.works(offset=offset)
    pbar.total = res["message"]["total-results"]
    for item in res["message"]["items"]:
        print(json.dumps(item))
        pbar.update()
    offset = offset + len(res["message"]["items"])
    if res["message"]["total-results"] == offset:
        break
