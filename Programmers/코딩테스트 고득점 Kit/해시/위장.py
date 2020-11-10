from collections import Counter

def solution(clothes):
    
    kind_lst = []
    
    for item, kind in clothes :
        kind_lst.append(kind)
        pass # append kinds
    
    count_kind = Counter(kind_lst)
    kinds = sorted(count_kind)
    num_kind = len(count_kind)
    answer = 1

    for i in kinds :
        count = count_kind[i]
        answer *= (count + 1)
        pass # calculate

    answer = answer - 1
    return answer
