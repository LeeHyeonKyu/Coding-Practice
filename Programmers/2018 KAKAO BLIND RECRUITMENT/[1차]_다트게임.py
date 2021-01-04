def solution(dartResult:str) -> int :
    answer = '0'
    prev_idx = 1
    curr = '+'
    for val in dartResult :
        if val.isdigit() :
            curr += val
        elif val.isalpha() :
            prev_idx = len(answer)
            answer += curr
            curr = '+'
            if val == 'S' :
                answer += '**1'
            elif val == 'D' :
                answer += '**2'
            elif val == 'T' :
                answer += '**3'
        else :
            if val == '*' :
                answer = answer[:prev_idx] + '*2' + answer[prev_idx:]
                answer += '*2'
            elif val == '#' :
                answer += '*(-1)'

    return eval(answer)
