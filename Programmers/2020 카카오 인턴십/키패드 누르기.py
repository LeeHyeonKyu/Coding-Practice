def solution(numbers, hand):
    answer = ''
    numbers = list(map(lambda x : x-1 if x != 0 else 10, numbers))
    L = (3, 0)
    R = (3, 2)
    for num in numbers :
        tmp = divmod(num, 3)
        if tmp[1] == 0 :
            answer += 'L'
            L = tmp
        elif tmp[1] == 2 :
            answer += 'R'
            R = tmp
        else :
            L_dist = abs(L[0]-tmp[0]) + abs(L[1]-tmp[1])
            R_dist = abs(R[0]-tmp[0]) + abs(R[1]-tmp[1])
            if (L_dist == R_dist and hand == 'right') or L_dist > R_dist : 
                answer += 'R'
                R = tmp
            elif (L_dist == R_dist and hand == 'left') or L_dist < R_dist : 
                answer += 'L'
                L = tmp
        
    return answer
