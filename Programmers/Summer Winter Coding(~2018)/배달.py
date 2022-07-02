from collections import defaultdict
import heapq

def solution(N, road, K):
    road_map = defaultdict(lambda: defaultdict(lambda: float('inf')))
    for lst in road:
        a, b, cost = lst
        road_map[a][b] = min(road_map[a][b], cost)
        road_map[b][a] = min(road_map[b][a], cost)
    
    goal_map = defaultdict(lambda: float('inf')) # key=goal, val=cost
    stack = [(1, 0)] # start, cost
    while stack:
        start, accum_cost = stack.pop()
        for goal, cost in road_map[start].items():
            if accum_cost + cost < goal_map[goal]:
                goal_map[goal] = accum_cost + cost
                stack.append((goal, accum_cost + cost))
    
    answer = set([1])
    for goal, cost in goal_map.items():
        if cost <= K:
            answer.add(goal)
    return len(answer)