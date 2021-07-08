import sys
from collections import deque

def main(start: int, end: int) -> int:
    answer = float('inf')
    queue = deque()
    queue.append((start+1, 1, 1))

    while queue:
        position, speed, cnt = queue.popleft()
        if position == end and speed == 1:
            answer = min(cnt, answer)
        else:
            for sp in [speed, speed+1]:
                if position+sp <= end:
                    queue.append((position+sp, sp, cnt+1))

        for i in range(1, speed):
            position += i
            cnt += 1
        if position == end:
            answer = min(cnt, answer)

    return answer

input = sys.stdin.readline
k = int(input())
for _ in range(k):
    start, end = list(map(int, input().split()))
    print(main(start, end))