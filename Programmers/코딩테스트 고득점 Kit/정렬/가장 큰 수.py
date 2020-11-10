from itertools import chain, repeat

def solution(numbers):
    answer = ''
    # 숫자 문자열로 변환
    str_numbers = [ str(val) for val in numbers]
#     str_numbers = list(map(str, numbers))    
    dict_numbers = dict()
    
#     repeat_numbers = [ repeat(num, 2) if len(num) >=2 else repeat(num, 4) for key, num in enumerate(str_numbers)]
#     print(repeat_numbers)
    
#     # 문자열 리스트 정렬
#     for idx, num in enumerate(str_numbers) :
#         if len(num) >=2  :
#             dict_numbers[idx] = int(''.join(repeat(num, 2)) )
#         else :
#             dict_numbers[idx] = int(''.join(repeat(num, 4)) )
    for idx, num in enumerate(str_numbers) :
        if len(num) == 1 :
            dict_numbers[idx] = int(num*4)
        elif len(num) == 2:
            dict_numbers[idx] = int(num*2) 
        elif len(num) == 3 :
            dict_numbers[idx] = int(num+num[0])
        else :
            dict_numbers[idx] = int(num)

    
    # dict 값으로 정렬
    dict_numbers = sorted(dict_numbers.items(), key=(lambda x : x[1]), reverse=True)

    str_keys = ''
    for key in dict_numbers:
        str_keys += str_numbers[key[0]]
    answer = str(int(str_keys))

            # 비교
    return answer
