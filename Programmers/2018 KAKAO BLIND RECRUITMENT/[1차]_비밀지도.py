def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        tmp = bin(arr1[i] | arr2[i])
        tmp = tmp[2:].zfill(n)
        answer.append(tmp.replace('1', '#').replace('0', ' '))
    return answer
