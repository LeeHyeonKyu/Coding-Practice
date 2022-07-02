from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    order_dict = defaultdict(int)
    cnt_dict = defaultdict(int)
    
    for order in orders:
        order = ''.join(sorted(list(order)))
        for c in course:
            combination_results = combinations(order, c)
            for combination_result in combination_results:
                combination_result = ''.join(combination_result)
                order_dict[combination_result] += 1
                cnt_dict[c] = max(cnt_dict[c], order_dict[combination_result])
    
    return sorted([key for key, val in order_dict.items() if val == cnt_dict[len(key)] and val >= 2])