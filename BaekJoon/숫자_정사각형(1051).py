import sys
from collections import defaultdict

def main(n, m, board):
    dic = defaultdict(list)
    for y_idx, line in board:
        for x_idx, num in line:
            dic[num].append((y_idx, x_idx))
    return 

input = sys.stdin.readline
n, m = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(input())
print(main(n, m, board))