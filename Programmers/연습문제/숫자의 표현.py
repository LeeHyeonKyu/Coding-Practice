def solution(n):
    answer = 0
    for i in range(1, n//2 + 2):
        x = (n - (i*(i-1))/2) / i
        if x == int(x) and x > 0:
            answer += 1
    return answer