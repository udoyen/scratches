def my_check(s: str):

    is_valid = True

    s1 = ['[', ']']
    s2 = ['{', '}']
    s3 = ['(', ')']

    sm = [s1, s2, s3]

    for i in s:
        for n in sm:
            if i in n:
                n.pop(n.index(i))

    for k in sm:
        if len(k) == 1:
            is_valid = False

    return is_valid


my_check('[{}]')


