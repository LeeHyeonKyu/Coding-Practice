def solution(numbers):
    answer_set = set()
    
    for idx, a in enumerate(numbers) :
        for b in numbers[idx+1:] :
            answer_set.add(a+b)
            
    answer = sorted(list(answer_set))
    return answer
