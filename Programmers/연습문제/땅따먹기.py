def solution(land):
    answer = 0
    stack = [(0, 0, 5)]
    while stack:
        val, row_idx, prev_num_idx = stack.pop()
        if row_idx == len(land):
            answer = max(answer, val)
        else:
            for num_idx, num in enumerate(land[row_idx]):
                if prev_num_idx != num_idx:
                    stack.append((val+num, row_idx+1, num_idx))
    
    return answer