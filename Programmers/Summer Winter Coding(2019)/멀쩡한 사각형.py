from math import ceil, floor

def solution(w, h):
    tot = w * h
    inclination = h/w
    cutted = 0
    prev = 0
    for i in range(1, w+1):
        now = inclination * i
        cutted += ceil(now) - floor(prev)
        prev = now
        if int(now) == now:
            cutted *= w/i
            break
    
    return tot - cutted