def search(place, line_idx, seat_idx):
    if seat_idx + 1 < 5:
        r1 = place[line_idx][seat_idx+1]
        if r1 == 'P':
            return False
        elif r1 == 'O':
            if seat_idx + 2 < 5:
                r2 = place[line_idx][seat_idx+2]
                if r2 == 'P':
                    return False
            if line_idx + 1 < 5:
                r1b1 = place[line_idx+1][seat_idx+1]
                if r1b1 == 'P':
                    return False
            if line_idx - 1 >= 0:
                r1t1 = place[line_idx-1][seat_idx+1]
                if r1t1 == 'P':
                    return False
    
    if line_idx + 1 < 5:
        b1 = place[line_idx+1][seat_idx]
        if b1 == 'P':
            return False
        elif b1 == 'O':
            if line_idx + 2 < 5:
                b2  = place[line_idx+2][seat_idx]
                if b2 == 'P':
                    return False
            if seat_idx + 1 < 5:
                b1r1 = place[line_idx+1][seat_idx+1]
                if b1r1 == 'P':
                    return False
            if seat_idx - 1 >= 0:
                b1l1 = place[line_idx+1][seat_idx-1]
                if b1l1 == 'P':
                    return False
    
    if seat_idx - 1 >= 0:
        l1 = place[line_idx][seat_idx-1]
        if l1 == 'O':
            if line_idx + 1 < 5:
                l1b1 = place[line_idx+1][seat_idx-1]
                if l1b1 == 'P':
                    return False
    
    if line_idx - 1 >= 0:
        t1 = place[line_idx-1][seat_idx]
        if t1 == 'O':
            if seat_idx + 1 < 5:
                t1r1 = place[line_idx-1][seat_idx+1]
                if t1r1 == 'P':
                    return False
    
    return True

def solution(places):
    answer = [1] * len(places)
    for place_idx, place in enumerate(places):
        for line_idx, line in enumerate(place):
            for seat_idx, seat in enumerate(line):
                flag = True
                if seat == 'P':
                    flag = search(place, line_idx, seat_idx)
                    if flag == False:
                        answer[place_idx] = 0
                if not flag:
                    break
            if not flag:
                break
    
    return answer