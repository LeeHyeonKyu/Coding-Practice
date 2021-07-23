def recursive(n, row, col):
    global flag
    global cnt
    if flag:
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

cnt = 0
flag = False
N, r, c = list(map(int, input().split()))
recursive(2 ** N, 0, 0)