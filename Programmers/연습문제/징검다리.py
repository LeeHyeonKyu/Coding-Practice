def solution(distance, rocks, n):
    start, end = 0, distance
    rocks.append(distance)
    rocks.sort()
    
    while start <= end:
        mid = (start + end) // 2
        removed_stone = 0
        prev_stone = 0
        for rock in rocks:
            if rock - prev_stone < mid:
                removed_stone += 1
            else:
                prev_stone = rock
                
        if removed_stone > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
                    
    return answer