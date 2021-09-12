import math

def chk_devisor(num):
    limit = math.ceil(math.sqrt(num))
    result = set()
    for i in range(1, limit+1):
        q, r = divmod(num, i)
        if r == 0:
            result.add(q)
            result.add(i)
    if len(result) % 2 == 0:
        result = num
    else:
        result = -num
    return result


def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        result = chk_devisor(num)
        answer += result
    return answer