def calc_max(base, new):
    tmp1 = max(base[0], new[0]), max(base[1], new[1])
    tmp2 = max(base[0], new[1]), max(base[1], new[0])
    return tmp1 if tmp1[0] * tmp1[1] < tmp2[0] * tmp2[1] else tmp2

def solution(sizes):
    result = [(0,0), (0,0)]
    for t1, t2 in sizes:
        result[0] = calc_max(result[0], (t1, t2))
        result[1] = calc_max(result[1], (t2, t1))
    return min(result[0][0] * result[0][1], result[1][0] * result[1][1])