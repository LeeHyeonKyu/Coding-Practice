import itertools

def cal(oper, ex_lst) :
    temp_lst = ex_lst[:]

    for op in oper :
        while True :
            try :
                op_idx = temp_lst.index(op)
                temp_str = ''.join(temp_lst[op_idx-1:op_idx+2])
                temp_val = int(eval(temp_str))
                del(temp_lst[op_idx-1])
                del(temp_lst[op_idx-1])
                del(temp_lst[op_idx-1])
                temp_lst.insert(op_idx-1, str(temp_val))
            except :
                break
            pass
        pass
    
    return abs(int(temp_lst[0]))

def solution(expression) :
    ex_split_lst = []
    slice_point = 0
    operator_lst = list(itertools.permutations('*+-', 3))
    answer_lst = []

    for idx, numorop in enumerate(expression) :
        if numorop.isdigit() == False :
            ex_split_lst.append(expression[slice_point:idx])
            ex_split_lst.append(numorop)
            slice_point = idx+1
            pass
        if idx == len(expression)-1 :
            ex_split_lst.append(expression[slice_point:idx+1])
            pass
        pass

    for oper in operator_lst :
        temp_result = cal(oper, ex_split_lst)
        answer_lst.append(temp_result)
        pass
    
    return max(answer_lst)
