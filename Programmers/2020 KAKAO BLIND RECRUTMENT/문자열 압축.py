def solution(s):
    tot_len = len(s)
    answer_lst = []
    
    for window_size in range(1, (tot_len//2)+2) :
        start_point = 0
        duplicate_cnt = 0
        window_result = tot_len
        
        while start_point + window_size <= tot_len :
            front = s[start_point : start_point + window_size]
            back = s[start_point + window_size : start_point + (2 * window_size)]
            if front == back :
                duplicate_cnt += 1
            elif duplicate_cnt >= 1 :
                window_result = window_result - (duplicate_cnt * window_size) + len(str(duplicate_cnt+1))
                duplicate_cnt = 0
            start_point += window_size
        
        answer_lst.append(window_result)
    
    return min(answer_lst)
