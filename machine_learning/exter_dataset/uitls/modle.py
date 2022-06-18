def midline(in_=None,out_=None,middle=None):
    d = {}
    if in_ is not None:
        d["in"] = in_
    if out_ is not None:
        d["out"] = out_
    if middle is not None:
        d["middle"] = middle
    return d 




def or_same(*args):
    return {
        "type":"or_same",
        "var":args
    }

def or_diff(*args):
    return {
        "type":"or_diff",
        "var":args
    }