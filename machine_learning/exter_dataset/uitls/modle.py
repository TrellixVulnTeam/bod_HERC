def mideline(in_=None,out_=None,middle=None):
    return {
        "in":in_,
        "out_":out_,
        "middle":middle,
    }


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