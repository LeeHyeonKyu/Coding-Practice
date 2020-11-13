def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)
    result_lst = []
    for i in range(len(arr)-1) :
        result = sorted_arr[i] - sorted_arr[i+1]
        result_lst.append(abs(result))
    return min(result_lst)
