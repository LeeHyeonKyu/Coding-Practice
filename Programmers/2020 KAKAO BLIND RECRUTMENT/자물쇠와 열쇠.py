def rot(one_point, M):
    return set([(j, M-i-1) for i,j in one_point])

def shift(one_point, r_shift, c_shift, N):
    shift_result = set()
    for i, j in one_point:
        i += r_shift
        j += c_shift
        if not (i < 0 or i >= N or j < 0 or j >= N):
            shift_result.add((i,j))
    return shift_result

def solution(key, lock):
    M, N = len(key), len(lock)
    
    zero_point = set()
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                zero_point.add((i,j))
    
    one_point = set()
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                one_point.add((i,j))
    
    for _ in range(4):
        one_point = rot(one_point, M)
        for r_shift in range(-N, N+1):
            for c_shift in range(-N, N+1):
                shift_result = shift(one_point, r_shift, c_shift, N)
                if shift_result == zero_point:
                    return True
    return False