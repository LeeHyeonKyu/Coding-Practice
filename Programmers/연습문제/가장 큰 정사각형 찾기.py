class Square():
    def __init__(self):
        self.r1 = -1
        self.r2 = -1
        self.c1 = -1
        self.c2 = -1
        self.tot = 0
    
    def renew(self, r1, r2, c1, c2, tot):
        self.r1 = r1
        self.r2 = r2
        self.c1 = c1
        self.c2 = c2
        self.tot = tot

def solution(board):
    max_r = len(board)
    max_c = len(board[0])
    big_one = Square()
    
    for r, line in enumerate(board):
        for c, dot in enumerate(line):
            if dot == 1 and not (r >= big_one.r1 and r <= big_one.r2) and not (c >= big_one.c1 and r <= big_one.c2) :
                
                r2, c2 = r, c
                while r2+1 < max_r and c2+1 < max_c:
                    tmp = board[r:r2+2][c:c2+2]
                    tmp_tot = sum([tmp_line.count(1) for tmp_line in tmp])
                    if tmp_tot == ((r2+2 - r) * (c2+2 - c)):
                        r2 += 1
                        c2 += 1
                    else:
                        break
                
                if ((r2+2 - r) * (c2+2 - c)) > big_one.tot:
                    big_one.renew(r, r2, c, c2, ((r2+2 - r) * (c2+2 - c)))
    
    return big_one.tot