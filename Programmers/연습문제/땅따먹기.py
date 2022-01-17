from collections import defaultdict

def solution(land):
    lst = [(5, 0)]
    for line in land:
        val_dict = defaultdict(int)
        for idx, val in enumerate(line):
            for prev_idx, prev_val in lst:
                if idx != prev_idx:
                    val_dict[idx] = max(val_dict[idx], prev_val+val)
        lst = sorted(list(val_dict.items()), key=lambda x: -x[1])[:2]
    return lst[0][1]