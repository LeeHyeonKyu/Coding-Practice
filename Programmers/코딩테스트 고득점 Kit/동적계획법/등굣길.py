from collections import deque

def solution(m, n, puddles):
    puddles = set(map(lambda x: tuple(x), puddles))
    queue = deque([(1,1)])
    answer = 0
    
    while queue:
        point = queue.popleft()
        i, j = point
        if i == m and j == n:
            answer += 1
        elif point not in puddles:
            if i < m:
                queue.append((i+1, j))
            if j < n:
                queue.append((i, j+1))
    
    return answer % 1000000007