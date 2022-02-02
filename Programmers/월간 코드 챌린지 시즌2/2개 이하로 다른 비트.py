def bit_op(num):
    bit = bin(num)[2:]
    for i in range(1, min(3, len(bit))+1):
        if bit[-i] == '0':
            return num+1
    
    cnt = 0
    for i in bit[::-1]:
        if i == '1':
            cnt +=1
        else:
            break
    result = bin(num+1)[2:]
    if len(result) == len(bit):
        result = result[:-cnt] + '00' + ('1' * (cnt-2))
    else:
        result = result[:-cnt] + '0' + ('1' * (cnt-1))
    return int(result, 2)

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(bit_op(num))
    return answer