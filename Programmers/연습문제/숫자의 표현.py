def solution(n):
    answer = 0
    lst = range(1, n+1)
    for window_size in lst:
        i = 0
        while i + window_size <= n:
            if sum(lst[i:i+window_size]) == n:
                print(lst[i:i+window_size])
                answer += 1
                break
            i += 1
    return answer