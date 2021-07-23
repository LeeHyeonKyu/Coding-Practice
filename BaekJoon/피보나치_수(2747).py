def fib(n):
    lst = [0, 1]
    length = 2
    while length <= n:
        lst.append(lst[length-1] + lst[length-2])
        length += 1
    return lst[n]

n = int(input())
print(fib(n))