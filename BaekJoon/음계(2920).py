def main(lst: list) -> str:
    sort_flag = True
    if lst[0] > lst[-1]:
        lst = lst[::-1]
        rev_flag = True
    else:
        rev_flag = False
    
    for idx in range(1, len(lst)):
        if lst[idx] - lst[idx-1] != 1:
            sort_flag = False
            break
    
    if sort_flag:
        if rev_flag:
            answer = 'descending'
        else:
            answer = 'ascending'
    else:
        answer = 'mixed'
    return answer

lst = list(map(int, input().split()))
print(main(lst))