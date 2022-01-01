from collections import Counter

def get_primes(num):
    flags = ([False] * 2) + ([True] * (num - 1))
    primes = []
    for i, flag in enumerate(flags):
        if flag:
            primes.append(i)
            j = 2
            while i * j < num:
                flags[i*j] = False
                j += 1
    return primes

def solution(arr):
    primes = get_primes(max(arr))
    counters = []
    for num in arr:
        counter = Counter()
        while num != 1:
            for prime in primes:
                q, r = divmod(num, prime)
                if r == 0:
                    num = q
                    counter[prime] += 1
        counters.append(counter)
    
    result_counter = Counter()
    for counter in counters:
        for key, val in counter.items():
            result_counter[key] = max(result_counter[key], counter[key])
    
    answer = 1
    for key, val in result_counter.items():
        answer *= (key ** val)
    return answer