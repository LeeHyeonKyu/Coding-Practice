def solution(n, times) :
    times.sort(reverse=False)
    answer = 0
    left = 0
    right = times[-1] * n
    while left <= right :
        cnt = 0
        mid = (left+right)//2
        for time in times :
            cnt += mid // time
        
        if cnt < n :
            left = mid + 1
        elif cnt >= n :
            right = mid - 1
            if answer == 0 :
                answer = mid
            else :
                answer = min(answer, mid)
        
    return answer
