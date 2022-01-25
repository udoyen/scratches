def is_anagram(fstring, sstring):
    if len(fstring) == len(sstring):
        s = list(sstring)
        for i in list(fstring):
            if i in s:
                s.pop(s.index(i))
            else:
                return False
    return True


is_anagram('test', 'tess')
