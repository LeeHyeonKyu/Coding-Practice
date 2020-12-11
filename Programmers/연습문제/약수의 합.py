def solution(n):
    if n == 0 :
        return 0
    answer = set()
    for i in range(1, (n//2)+2) :
        q, r = divmod(n, i)
        if r == 0 :
            answer.add(q)
            answer.add(i)
    return sum(answer)
