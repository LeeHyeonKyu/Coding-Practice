def alternatingCharacters(s):
    cnt = 0
    prev = ''
    for i in s :
        if i == prev :
            cnt += 1
        else :
            prev = i
    return cnt
