def solution(triangle) :
    i = len(triangle)-1
    if i == 0 :
        return(triangle[0])
    else :
        floor = [max(triangle[i][x], triangle[i][x+1]) for x in range(len(triangle[i])-1)]
        while True :
            floor = [x+y for x,y in zip(floor, triangle[i-1])]
            i -= 1
            if i == 0 :
                break
            floor = [max(floor[x], floor[x+1]) for x in range(len(floor)-1)]
    
    return floor[0]
