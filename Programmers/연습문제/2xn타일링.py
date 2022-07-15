def solution(n):
    answer = 0
    m = n//2
    cnt1 = 1
    cnt2 = 2
    if n==1:
        return cnt1
    elif n==2:
        return cnt2
    for i in range(n-2):
        cnt1, cnt2 = cnt2, cnt2+cnt1
    return cnt2%1000000007