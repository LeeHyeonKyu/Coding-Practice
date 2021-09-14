import heapq

def solution(d, budget):
    heapq.heapify(d)
    answer = 0
    while d:
        require_budget = heapq.heappop(d)
        if budget >= require_budget:
            answer += 1
            budget -= require_budget
        else:
            break
    return answer