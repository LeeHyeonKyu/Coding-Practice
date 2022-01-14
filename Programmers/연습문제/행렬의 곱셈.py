def solution(arr1, arr2):
    r_limit = len(arr1)
    c_limit = len(arr1[0])
    result = []
    for r in range(r_limit):
        tmp_lst = []
        tmp = 0
        for c in range(c_limit):
            tmp += arr1[r][c] * arr2[c][r]
        tmp_lst.append(tmp)
    return result