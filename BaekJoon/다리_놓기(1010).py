import sys

def main(N: int, M: int) -> int:
    answer = 1
    for i in range(M, M-N, -1):
        answer *= i
    for i in range(N, 1, -1):
        answer //= i
    return int(answer)

input = sys.stdin.readline
k = int(input())
for _ in range(k):
    N, M = list(map(int, input().split()))
    print(main(N, M))
