from collections import Counter

def solution(lottos, win_nums):
    correct_nums = len(set(win_nums).intersection(lottos))
    zeros = Counter(lottos)[0]
    maximum = 7 - (correct_nums + zeros) if 7 - (correct_nums + zeros) < 7 else 6
    minimum = 7 - correct_nums if 7 - correct_nums < 7 else 6
    return [maximum, minimum]