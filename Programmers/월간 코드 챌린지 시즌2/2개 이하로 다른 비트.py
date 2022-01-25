def bit_op(num):
    bit = bin(num)[2:]
    if bit[-1] == '0':
        return num+1
    elif bit[-2] == '0':
        return num+1
    elif bit[-3] == '0':
        return num+1
    
    cnt = 0
    for i in bit[::-1]:
        if i == '1':
            cnt +=1
        else:
            break
    result = bin(num+1)
    result = result[:-cnt] + '00' + ('1' * (cnt-2))
    return int(result, 2)

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(bit_op(num))
    return answer

solution([7])