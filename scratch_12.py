def zap(flist, slist):
    result = []
    for i, v in enumerate(flist):
        result.append((v, slist[i]))
    return result


zap([1, 3], [2, 4])
