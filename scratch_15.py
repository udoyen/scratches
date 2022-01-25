def  find(N, trust):
    if len(trust) == 1:
        result = trust[0][1]
        return result
    else:
        result = trust[-1]

    for i in range(0, len(trust)):
        if result == trust[i][2]:
            continue
        else:
            result = -1
            return result



    return result