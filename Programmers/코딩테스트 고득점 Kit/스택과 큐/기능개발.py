import numpy as np

def solution(progresses, speeds):
    
    answer = []
    prog_ndarray = np.array(progresses)
    sp_ndarray = np.array(speeds)
    
    while list(prog_ndarray) :
        if prog_ndarray[0] >= 100 :
            count_ndarray = (prog_ndarray >= 100)
            count = 0
            for bools in count_ndarray :
                if bools == True :
                    count += 1
                else :
                    break
            answer.append(count)
            prog_lst = list(prog_ndarray)
            sp_lst = list(sp_ndarray)
            del(prog_lst[:count])
            del(sp_lst[:count])
            prog_ndarray = np.array(prog_lst)
            sp_ndarray = np.array(sp_lst)
        else :
            prog_ndarray = prog_ndarray + sp_ndarray
    
    return answer
