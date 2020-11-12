# recursive func
def solution(x) : 
    if x <= 1 :
        return x
    else :
        return solution(x-1) + solution(x-2)

# iterative func
def solution(x) :
    cnt = -1
    fib_lst = []
    while cnt != x :
        cnt += 1
        if cnt <= 1 :
            fib_lst.append(cnt)
        else :
            new_val = fib_lst[cnt-2] + fib_lst[cnt-1]
            fib_lst.append(new_val)
    return fib_lst[cnt]
