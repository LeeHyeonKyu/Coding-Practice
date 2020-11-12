def solution(L, x) :
    left = 0
    right = len(L)-1
    answer = -1

    while left <= right :
        middle = (left + right) // 2
        if L[middle] == x :
            answer = middle
            break
        elif L[middle] < x :
            left = middle + 1
        elif L[middle] > x :
            right = middle - 1

    return answer
