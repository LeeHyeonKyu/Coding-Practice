def solution(n):
    answer = ''
    while n > 0 :
        q, r = divmod(n, 3)
        if r == 0 :
            q -= 1
            r = 3
        if r == 3 :
            answer += '4'
        else :
            answer += str(r)
        n = q
	
    answer = answer[::-1]
    return answer
