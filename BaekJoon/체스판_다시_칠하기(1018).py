import sys

def check_block(y_idx: int, x_idx: int, pivot: int) -> int:
    cnt = 0
    if (y_idx + x_idx) % 2 == 0:
        if board[y_idx][x_idx] == pivot:
            cnt += 0
        else:
            cnt += 1
    elif (y_idx + x_idx) % 2 != 0:
        if board[y_idx][x_idx] == pivot:
            cnt += 1
        else:
            cnt += 0
    return cnt

def check_board(start_y: int, start_x: int) -> int:
    lst = []
    w_cnt, b_cnt = 0, 0
    for y in range(8):
        for x in range(8):
            w_cnt += check_block(start_y+y, start_x+x, 'W')
            b_cnt += check_block(start_y+y, start_x+x, 'B')
    lst.append(w_cnt)
    lst.append(b_cnt)
    return min(lst)

def main(n: int, m: int) -> int:
    cnt_lst = []
    for start_y in range(n-7):
        for start_x in range(m-7):
            cnt_lst.append(check_board(start_y, start_x))
    return min(cnt_lst)

input = sys.stdin.readline
n, m = list(map(int, input().split()))
board = []
for _ in range(n):
    line = input()
    board.append(line)
print(main(n, m))