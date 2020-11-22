def solution(a, b):
    answer = 0
    for idx, an in enumerate(a) : 
        answer += (an * b[idx])
    return answer
