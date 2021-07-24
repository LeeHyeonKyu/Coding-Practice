from collections import defaultdict

dic = defaultdict(int)

N = int(input())

for _ in range(N):
    book = input()
    dic[book] += 1

lst = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(lst[0][0])