from math import ceil

def solution(w, h):
    x, r = 0, -1
    while r != 0:
        x += 1
        q, r = divmod(h*x, w)
        
    return (w*h) - (w*ceil(h/w))