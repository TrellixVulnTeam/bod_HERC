def fuzzy_NOT(x):
    return 1-x


def fuzzy_AND(*args):
    return min(args)


def fuzzy_OR(*args):
    return max(args)
