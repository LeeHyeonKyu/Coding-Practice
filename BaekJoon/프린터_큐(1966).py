import sys
from collections import deque

def main(n, target_idx, lst):
    cnt = 0
    idx_q = deque(range(n))
    imp_q = deque(lst)
    max_imp = max(imp_q)
    while imp_q:
        idx = idx_q.popleft()
        imp = imp_q.popleft()
        if imp == max_imp:
            cnt += 1
            if idx == target_idx:
                break
            max_imp = max(imp_q)
        else:
            idx_q.append(idx)
            imp_q.append(imp)
    return cnt

input = sys.stdin.readline
k = int(input())
for _ in range(k):
    n, target_idx = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    print(main(n, target_idx, lst))