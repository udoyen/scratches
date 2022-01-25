def double_letters(letters):
    for i in letters:
        if letters.index(i) != (len(letters) - 1):
            if i.lower() == letters[letters.index(i) + 1].lower():
                return True
        continue
    return False


double_letters("on and off")
