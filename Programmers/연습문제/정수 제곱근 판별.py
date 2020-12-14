from math import sqrt

def solution(n):
    route_n = sqrt(n)
    if int(route_n) == route_n :
        return n + (2*route_n) + 1
    else :
        return -1
