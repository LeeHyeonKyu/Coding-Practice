def solution(m, n, board):
    erase_blocks = set()
    answer = 0
    board = [list(line) for line in board]
    while True :
        # 터트릴 블록 확인
        for y in range(m-1) :
            for x in range(n-1) :
                if board[y][x] != '#' and \
                    board[y][x] == board[y][x+1] and \
                    board[y][x] == board[y+1][x] and \
                    board[y][x] == board[y+1][x+1] :
                    erase_blocks.add((y, x))
                    erase_blocks.add((y, x+1))
                    erase_blocks.add((y+1, x))
                    erase_blocks.add((y+1, x+1))
        
        # 블록 터트리기
        for y, x in erase_blocks :
            board[y][x] = '#'
            answer += 1
            
        # 위부터 순회하며 블록 내리기
        for _ in range(m) :
            for y in range(m-1) :
                for x in range(n) :
                    if board[y+1][x] == '#' :
                        board[y+1][x], board[y][x] = board[y][x], board[y+1][x]
        
        # 종료 조건
        if not erase_blocks :
            break
        else :
            erase_blocks = set()

    return answer
