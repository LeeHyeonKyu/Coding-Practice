def solution(arr1, arr2):
    r_limit = len(arr1)
    c_limit = len(arr1[0])
    result = []
    for l in range(l_limit):
        tmp_lst = []
        tmp = 0
        for c in range(l_limit):
            tmp += arr1[l][c] * arr2[c][l]
        tmp_lst.append(tmp)
    return result