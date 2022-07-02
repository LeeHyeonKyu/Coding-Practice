from collections import defaultdict, deque

def solution(n, edges):
    node_map = defaultdict(list)
    for a, b in edges:
        node_map[a].append(b)
        node_map[b].append(a)
    
    queue = deque()
    queue.append([1, 0]) # start node, dist
    max_dist = 0
    dist_dict = defaultdict(lambda: float('inf'))
    while queue:
        node, dist = queue.popleft()
        if node in dist_dict:
            continue
        else:
            dist_dict[node] = min(dist, dist_dict[node])
            max_dist = max(dist, max_dist)
            for arrive in node_map[node]:
                if arrive not in dist_dict:
                    queue.append([arrive, dist+1])
    
    answer = 0
    for val in dist_dict.values():
        if val == max_dist:
            answer += 1
    return answer