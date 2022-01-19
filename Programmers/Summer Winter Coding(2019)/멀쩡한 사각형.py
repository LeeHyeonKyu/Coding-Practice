from math import ceil

def solution(w, h):
    x, y, cnt, r = 0, 0, 0, -1
    while r != 0:
        x += 1
        tmp = (h/w)*x
        cnt += ceil(tmp-int(y))
        y = tmp
        q, r = divmod(h*x, w)
    return (w*h)-(cnt*(h/q))