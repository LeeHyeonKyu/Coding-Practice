def solution(board, moves):
    stack = []
    n_width = len(board)
    cnt = 0

    for i in moves :
        for line in board :
            pickup = line[i-1]
            if pickup != 0 :
                line[i-1] = 0
                break
                pass
            pass

        if pickup != 0:
            stack.append(pickup)
            pass

        if len(stack) >= 2 :
            if stack[-1] == stack[-2] :
                stack.pop()
                stack.pop()
                cnt += 2
                pass
            pass
        pass

    return cnt
