def solution(participant, completion):
    
    if set(participant) != set(completion) :
        answer = set(participant) - set(completion)
        return list(answer)[0]
        
    else :
        participant.sort()
        completion.sort()
        for i, man in enumerate(participant) :
            if completion[i] == man :
                continue
            else :
                return man
