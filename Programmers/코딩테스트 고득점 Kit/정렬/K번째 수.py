def solution(array, commands):

    answer = []

    for i, j, k in commands :
        slicing_array = array[ i-1 : j ]
        sorted_array = sorted(slicing_array)
        num = sorted_array[k-1]
        answer.append(num)

    return answer
