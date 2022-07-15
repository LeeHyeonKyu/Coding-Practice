def solution(n):
    n = n//2
    cnt1 = 3
    cnt2 = 11
    
    if n == 1:
        return cnt1
    elif n==2:
        return cnt2
    for i in range(n-2):
        cnt1, cnt2 = cnt2, cnt2+cnt1
    return cnt2