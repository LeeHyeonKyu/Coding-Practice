def solution(n):
    lst = [0, 1]
    while n >= len(lst):
        lst.append(lst[-1] + lst[-2])
    return lst[n] % 1234567