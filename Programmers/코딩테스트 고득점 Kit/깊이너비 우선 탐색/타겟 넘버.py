answer = 0
vector = []
state = []

def solve(start : int, end : int, cnt : int, numbers : list, target : int) -> None :
    global state, vector, answer
    
    if end == cnt :
        temp = numbers.copy()

        for i in vector :
            temp[i] *= -1

        sum = 0
        for i in temp :
            sum += i

        if sum == target :
            answer += 1

        return
        
    for idx in range(start, len(numbers)) :
        if state[idx] == 'Positive' :
            state[idx] = 'Negative'
            vector.append(idx)
            solve(idx, end, cnt+1, numbers, target)
            state[idx] = 'Positive'
            vector.pop()

def solution(numbers : list, target : int) -> int :
    global state, vector, answer

    state = ['Positive'] * len(numbers)
    
    for i in range(len(numbers)) :
        solve(0, i, 0, numbers, target)
        pass # end slove loop
    
    return answer
