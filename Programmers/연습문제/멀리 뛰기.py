def solution(n):
    lst = [1, 2]
    if n <= 2:
        return lst[n-1]
    
    for _ in range(n-2):
        lst[0], lst[1] = lst[1], lst[0]+lst[1]
    
    return lst[1] % 1234567