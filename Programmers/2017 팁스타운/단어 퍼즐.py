from collections import defaultdict, deque

def solution(strs, t):
    answer = float('inf')
    queue = deque([('',0)])
    str_map = defaultdict(list)
    for s in strs:
        str_map[s[0]].append(s)
    
    while queue:
        prev_str, cnt = queue.popleft()
        if prev_str == t:
            return cnt
        else:
            curr_str = t[len(prev_str)]
            for s in str_map[curr_str]:
                if t[len(prev_str):len(prev_str)+len(s)] == s:
                    queue.append((prev_str+s, cnt+1))
    
    return -1