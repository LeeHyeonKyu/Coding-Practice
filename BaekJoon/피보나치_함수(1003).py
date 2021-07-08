def solution(num) :
    lst = [(1,0), (0,1)]
    for i in range(num-1) :
        cnt0 = lst[i][0] + lst[i+1][0]
        cnt1 = lst[i][1] + lst[i+1][1]
        lst.append((cnt0, cnt1))
    print(lst[num][0], lst[num][1])

T = int(input())
for i in range(T) :
    N = int(input())
    solution(N)
