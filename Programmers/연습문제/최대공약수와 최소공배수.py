import math
from collections import defaultdict, Counter

def factorization(N, prime_lst):
    dic = defaultdict(int)
    while N != 1:
        for prime in prime_lst:
            q, r = divmod(N, prime)
            if r == 0:
                dic[prime] += 1
                N = q
                break
    return Counter(dic)

def get_prime(N):
    lst = [True] * (N+1)
    limit_n = math.ceil(math.sqrt(N))
    for i in range(2, limit_n):
        if lst[i]:
            j = 2
            while i*j <= N:
                lst[i*j] = False
                j += 1
    return [idx for idx, flag in enumerate(lst) if idx >= 2 and flag]

def calculate(factorized_N):
    result = 1
    for num, multiplier in factorized_N.items():
        result *= (num ** multiplier)
    return result

def solution(n, m):
    answer = [1, n*m]
    factorized_n = factorization(n, get_prime(n))
    factorized_m = factorization(m, get_prime(m))
    answer[0] = calculate(factorized_n & factorized_m)
    answer[1] = calculate(factorized_n | factorized_m)
    return answer