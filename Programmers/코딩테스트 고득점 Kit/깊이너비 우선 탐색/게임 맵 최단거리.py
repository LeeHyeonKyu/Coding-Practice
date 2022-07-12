from collections import defaultdict, deque

def solution(maps):
    dist_map = defaultdict(lambda: float('inf'))
    queue = deque([(0,0,1)])
    dist_map[(0, 0)] = 1
    n, m = len(maps)-1, len(maps[0])-1
    
    while queue:
        i, j, cnt = queue.popleft()
        cnt += 1
        for move in [-1, 1]:
            if (i+move >= 0 and i+move <= n) and \
                maps[i+move][j] == 1 and \
                dist_map[(i+move, j)] > cnt:
                dist_map[(i+move, j)] = cnt
                queue.append((i+move, j, cnt))
                
            if (j+move >= 0 and j+move <= m) and \
                maps[i][j+move] == 1 and \
                dist_map[(i, j+move)] > cnt:
                dist_map[(i, j+move)] = cnt
                queue.append((i, j+move, cnt))
    
    return dist_map[(n, m)] if dist_map[(n, m)] != float('inf') else -1