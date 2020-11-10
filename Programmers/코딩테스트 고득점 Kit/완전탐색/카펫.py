def solution(brown, yellow):
    
    answer = []
    total_num = yellow + brown
    highth = 0
    width = 0

    for i in list(range(2, total_num)) :
        highth = i
        width = brown*0.5 + 2 - i
        if highth * width == total_num :
            break
    
    answer.append(int(width))
    answer.append(highth)
    
    return answer
