from collections import Counter

def solution(s):
    loop_cnt, zero_cnt = 0, 0
    while s != '1':
        loop_cnt += 1
        counter = Counter(s)
        zero_cnt += counter['0']
        s = bin(int(counter['1']))[2:]
    return [loop_cnt, zero_cnt]