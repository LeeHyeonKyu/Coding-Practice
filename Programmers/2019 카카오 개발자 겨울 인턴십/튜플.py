from collections import Counter

def solution(s:str) -> tuple :
    count_updater = Counter([])
    tot_len = len(s)

    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.split(',')
    s = [int(x) for x in s]

    counter = Counter(s)
    answer = [x[0] for x in counter.most_common()]

    return answer
