import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for idx in range(N):
    age, name = list(sys.stdin.readline().split())
    age = int(age)
    heapq.heappush(heap, (age, idx, name))

while heap:
    age, idx, name = heapq.heappop(heap)
    print(age, name)