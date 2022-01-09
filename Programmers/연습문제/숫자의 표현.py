def solution(n):
    answer = 0
    for i in range(1, n):
        if i % 2 == 0 and (n-1) % i == 0 and sum(range(1, i+1)) <= n-1:
            answer += 1
        elif i % 2 == 1 and n % i == 0 and sum(range(1, i+1)) <= n:
            answer += 1
            
    return answer