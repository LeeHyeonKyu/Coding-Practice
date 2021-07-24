v, h = list(map(int, input().split()))
v_lst = [True] * v
h_lst = [True] * h

for v_idx in range(v):
    line = list(input())
    for h_idx, char in enumerate(line):
        if char == 'X':
            v_lst[v_idx] = False
            h_lst[h_idx] = False

print(max(sum(v_lst), sum(h_lst)))