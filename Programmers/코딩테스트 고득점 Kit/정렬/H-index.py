def solution(citations):
    
    answer = 0
    length = len(citations)
    over_array = []
    
    for i in range(length+1) :
        estimator = [x for x in citations if x >= i]
        if len(estimator) >= i :
            answer = i
            pass
        else : 
            break
        
    return answer
