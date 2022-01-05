def solution(s):
    s = s.split()
    s = list(map(int, s))
    s = sorted(s)
    tmp = str(s[0]), str(s[-1])
    return ' '.join(tmp)