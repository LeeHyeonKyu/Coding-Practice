def hourglassSum(arr):
    result_lst = []
    for i in range(1, 5) :
        for j in range(1, 5) :
            result = 0
            result += sum(arr[i-1][j-1:j+2])
            result += arr[i][j]
            result += sum(arr[i+1][j-1:j+2])
            result_lst.append(result)
    return max(result_lst)
