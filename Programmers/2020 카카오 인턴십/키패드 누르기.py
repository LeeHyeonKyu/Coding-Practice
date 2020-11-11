def solution(numbers:list, hand:str) -> str:
    L = '*'
    R = '#'
    answer_lst = []

    dict2 = {1:1, 2:0, 3:1, 4:2, 5:1, 6:2, 7:3, 8:2, 9:3, '*':4, 0:3, '#':4}
    dict5 = {1:2, 2:1, 3:2, 4:1, 5:0, 6:1, 7:2, 8:1, 9:2, '*':3, 0:2, '#':3}
    dict8 = {1:3, 2:2, 3:3, 4:2, 5:1, 6:2, 7:1, 8:0, 9:1, '*':2, 0:1, '#':2}
    dict0 = {1:4, 2:3, 3:4, 4:3, 5:2, 6:3, 7:2, 8:1, 9:2, '*':1, 0:0, '#':1}

    for num in numbers :
        if num in (1, 4, 7, '*') :
            answer_lst.append('L')
            L = num
        elif num in (3, 6, 9, '#') :
            answer_lst.append('R')
            R = num
        elif num in (2, 5, 8, 0) :
            if num == 2 :
                if dict2[R] > dict2[L] :
                    answer_lst.append('L')
                    L = num
                elif dict2[R] < dict2[L] :
                    answer_lst.append('R')
                    R = num
                elif dict2[R] == dict2[L] :
                    if hand == 'left' :
                        answer_lst.append('L')
                        L = num
                    else :
                        answer_lst.append('R')
                        R = num
            if num == 5 :
                if dict5[R] > dict5[L] :
                    answer_lst.append('L')
                    L = num
                elif dict5[R] < dict5[L] :
                    answer_lst.append('R')
                    R = num
                elif dict5[R] == dict5[L] :
                    if hand == 'left' :
                        answer_lst.append('L')
                        L = num
                    else :
                        answer_lst.append('R')
                        R = num
            if num == 8 :
                if dict8[R] > dict8[L] :
                    answer_lst.append('L')
                    L = num
                elif dict8[R] < dict8[L] :
                    answer_lst.append('R')
                    R = num
                elif dict8[R] == dict8[L] :
                    if hand == 'left' :
                        answer_lst.append('L')
                        L = num
                    else :
                        answer_lst.append('R')
                        R = num
            if num == 0 :
                if dict0[R] > dict0[L] :
                    answer_lst.append('L')
                    L = num
                elif dict0[R] < dict0[L] :
                    answer_lst.append('R')
                    R = num
                elif dict0[R] == dict0[L] :
                    if hand == 'left' :
                        answer_lst.append('L')
                        L = num
                    else :
                        answer_lst.append('R')
                        R = num

    answer = ''.join(answer_lst)

    return answer
