import collections

def solution(participant, completion):
    p_cnt = collections.Counter(participant)
    c_cnt = collections.Counter(completion)
    p_cnt.subtract(c_cnt)
    
    return list(p_cnt.elements())[0]
