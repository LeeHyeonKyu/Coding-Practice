def twoStrings(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    if set(s1) & set(s2) :
        return 'YES'
    else :
        return 'NO'
