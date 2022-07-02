def solution(n, a, b):
    cnt = 0
    while a != b:
        cnt += 1
        a = round(a/2+0.1)
        b = round(b/2+0.1)
        
    return cnt