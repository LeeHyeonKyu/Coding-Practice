def solution(x):
    num = 0
    for n in list(str(x)):
        num += int(n)
    return True if x%num==0 else False
