from itertools import permutations

def check(num_lst:list) -> int :
    temp_answer = 0
    for num in num_lst :
        switch = True
        if num == 2 :
            pass
        elif num < 2 :
            switch = False
            continue
        elif num % 2 == 0 :
            switch = False
            continue
        else :
            for j in range(3, num, 2) :
                if num % j == 0 :
                    switch = False
                    pass # 나눠지면 False
                pass # 3~num-1 홀수로 나눗셈
            pass # 소수인지 체크하는 if-elif-else
        
        if switch == True :
            temp_answer += 1
            pass # 위 조건을 통과하면 1 누적
        pass # num_lst의 모든 값 확인
    return temp_answer

def solution(numbers:str) -> int :
    answer = 0
    num_lst = []
    tot_len = len(numbers)
    
    for i in range(1, tot_len + 1) :
        combine_tuple = permutations(numbers, i)
        for combine_nums in combine_tuple :
            temp_int = int(''.join(combine_nums))
            num_lst.append(temp_int)
            pass # 조합된 값을 append
        pass # 위 과정을 len만큼 반복
    
    num_lst = list(set(num_lst))
    answer = check(num_lst)
    
    return answer
