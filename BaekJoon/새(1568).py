N = int(input())
cnt = 0
now = 1

while N != 0:
    if now <= N:
        N -= now
        cnt += 1
        now += 1
    else:
        now = 1
        N -= now
        cnt += 1
        now += 1

print(cnt)