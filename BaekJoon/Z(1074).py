def recursive(n, row, col):
    global cnt
    global flag
    if flag:
        return
    if not (row <= r and r < row + n and col <= c and c < col + n):
        cnt += int(n ** 2)
        return
    if n == 2:
        if row == r and col == c:
            print(cnt)
            flag += True
            return
        cnt += 1
        if row == r and col+1 == c:
            print(cnt)
            flag += True
            return
        cnt += 1
        if row+1 == r and col == c:
            print(cnt)
            flag += True
            return
        cnt += 1
        if row+1 == r and col+1 == c:
            print(cnt)
            flag += True
            return
        cnt += 1
        return
    recursive(n/2, row, col)
    recursive(n/2, row, col+n/2)
    recursive(n/2, row+n/2, col)
    recursive(n/2, row+n/2, col+n/2)

flag = False
cnt = 0
N, r, c = list(map(int, input().split()))
recursive(2 ** N, 0, 0)