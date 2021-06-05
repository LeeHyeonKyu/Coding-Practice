def solution(board, moves):
    stack = []
    answer = 0
    N = len(board)
    
    for move in moves :
        move -= 1
        for line in board :
            pick_up = line[move]
            if pick_up != 0 :
                line[move] = 0
                break
        
        if pick_up != 0 :
            stack.append(pick_up)
        
        if len(stack) >= 2 :
            if stack[-1] == stack[-2] :
                stack.pop()
                stack.pop()
                answer += 2
                
    return answer
