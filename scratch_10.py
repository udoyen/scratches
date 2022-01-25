def consecutive_zeros(bn):
    largest = 0
    count = []
    for i, v in enumerate(bn):
        if i == 0 and v == "1":
            continue
        if v == "0":
            largest += 1
            if len(bn) == 1:
                count.append(largest)
        if v == "1":
            count.append(largest)
            largest = 0
            continue
    largest = 0
    for j in count:
        if j > largest:
            largest = j
    return largest


def consecutive_zeros_simple(bin_str):
    return max([len(s) for s in bin_str.split("1")])


consecutive_zeros("0")
