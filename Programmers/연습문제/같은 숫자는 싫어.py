def solution(arr):
    answer = []
    p = ''
    for n in arr :
        if p == n :
            pass
        else :
            answer.append(n)
            p = n
    return answer
