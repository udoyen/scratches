# def all_equal(mlist):
#     return True if len({s for s in set(mlist)}) == 1 or 0 else False

def all_equal(mlist):
    result = len({s for s in set(mlist)})
    if result == 1 or result == 0:
        return True
    return False


all_equal([1, 1, 1])
