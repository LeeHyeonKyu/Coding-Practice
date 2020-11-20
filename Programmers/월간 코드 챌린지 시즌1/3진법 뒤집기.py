def solution(n):
    if n <= 2 :
        return n
    tmp_val = ''
    while n // 3 >= 1:
        remain = n % 3
        n = n // 3
        tmp_val = str(remain) + tmp_val
        if n < 3 :
            tmp_val = str(n) + tmp_val
    tmp_val = tmp_val[::-1]
    answer = int(tmp_val, 3)
    return answer
