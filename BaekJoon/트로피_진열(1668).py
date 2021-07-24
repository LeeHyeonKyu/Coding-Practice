N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))

max_l, max_r = 0, 0
cnt_l, cnt_r = 0, 0
for l, r in zip(lst, lst[::-1]):
    if max_l < l:
        cnt_l += 1
        max_l = l
    if max_r < r:
        cnt_r += 1
        max_r = r

print(cnt_l)
print(cnt_r)