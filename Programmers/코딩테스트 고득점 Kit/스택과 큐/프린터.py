def solution(priorities, location):
    
    answer = 0
    pr_array = priorities
    idx_array = list(range(len(priorities)))
    target = location
    count = 0
    
    while 1 :
        switch = True
        
        for num in pr_array :
            if pr_array[0] < num :
                switch = False
        
        if switch == False :
            del_num = pr_array[0]
            del_idx = idx_array[0]
            del(pr_array[0])
            del(idx_array[0])
            pr_array.append(del_num)
            idx_array.append(del_idx)
        else : 
            if idx_array[0] == target :
                answer = count + 1
                break
            else :
                count += 1
                del(pr_array[0])
                del(idx_array[0])
                
    return answer
