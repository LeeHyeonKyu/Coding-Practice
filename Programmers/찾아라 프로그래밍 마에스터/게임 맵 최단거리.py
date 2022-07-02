from collections import defaultdict

def solution(maps):
    n = len(maps)-1
    m = len(maps[0])-1
    discorved_map = defaultdict(lambda: float('inf'))
    
    stack = [(0,0,1)]
    while stack:
        r, c, cost = stack.pop()
        discorved_map[r,c] = cost
        if r-1 >= 0 and maps[r-1][c] == 1 and cost+1 < discorved_map[(r-1, c)]:
            stack.append((r-1, c, cost+1))
        if c-1 >= 0 and maps[r][c-1] == 1 and cost+1 < discorved_map[(r, c-1)]:
            stack.append((r, c-1, cost+1))
        if r+1 <= n and maps[r+1][c] == 1 and cost < discorved_map[(r+1, c)]:
            stack.append((r+1, c, cost+1))
        if c+1 <= m and maps[r][c+1] == 1 and cost < discorved_map[(r, c+1)]:
            stack.append((r, c+1, cost+1))
    
    return -1 if discorved_map[(n,m)] == float('inf') else discorved_map[(n,m)]