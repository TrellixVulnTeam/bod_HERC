wikidata_P_actions = {}
def P_actions_add(P,callback):
    if P not in wikidata_P_actions.keys():
        wikidata_P_actions[P]=[]
    wikidata_P_actions[P].append(callback)

def P_actions_remove(P,callback):
    pass