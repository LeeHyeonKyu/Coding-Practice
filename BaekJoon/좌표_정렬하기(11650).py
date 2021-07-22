import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(heap, (x, y))

while heap:
    x, y = heapq.heappop(heap)
    print(x, y)