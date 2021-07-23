import sys

N = int(sys.stdin.readline())
lst = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    lst[num] += 1

for idx in range(10001):
    for _ in range(lst[idx]):
        print(idx)