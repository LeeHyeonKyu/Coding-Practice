import math

def solution(n):
    lst = [False, False] + ([True] * (n-1))
    limit_n = math.ceil(math.sqrt(n))
    for i in range(limit_n+1):
        if lst[i]:
            j = 2
            while j*i <= n:
                lst[j*i] = False
                j += 1
    return sum(lst)