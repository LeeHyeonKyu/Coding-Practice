def solution(s):
    flag = True
    while flag:
        flag = False
        for idx in range(len(s)-1):
            if s[idx] == s[idx+1]:
                s = s[:idx] + s[idx+2:]
                flag = True
                break
    return 1 if s == '' else 0