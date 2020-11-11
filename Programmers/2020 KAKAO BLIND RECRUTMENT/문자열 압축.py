def solution(s) :
    tot_len = len(s)
    answer_lst = []

    for window_size in range(1, (tot_len//2)+2) :
        start_point = 0
        continue_cnt = 0
        window_result = tot_len

        while True :
            if start_point + window_size > tot_len :
                answer_lst.append(window_result)
                break # break point
            front = s[start_point : start_point + window_size]
            back = s[start_point + window_size : start_point + (2 * window_size)]
            if front == back :
                continue_cnt += 1
            elif continue_cnt >= 1 :
                window_result = window_result - (continue_cnt * window_size) + len(str(continue_cnt+1))
                continue_cnt = 0
                pass # end if-elif
            start_point += window_size
            pass # end while
        pass # end all loop
    
    return min(answer_lst)
