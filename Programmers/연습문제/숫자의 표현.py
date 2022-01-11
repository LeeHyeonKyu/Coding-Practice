def solution(n):
    answer = 0
    for i in range(1, n//2 + 2):
        x = (n - sum(range(i))) / i
        if x == int(x) and x > 0:
            answer += 1
    return answer