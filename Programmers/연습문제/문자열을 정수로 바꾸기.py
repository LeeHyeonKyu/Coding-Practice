def solution(s):
    if s.isdigit() or s[0] == '+':
        return int(s)
    else :
        return int(s[1:])*-1
