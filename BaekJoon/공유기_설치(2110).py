from bisect import bisect_left

def main(lst, N, C):
    lst.sort()
    low_gap = lst[1] - lst[0]
    high_gap = lst[-1] - lst[0]
    answer = 0

    while low_gap <= high_gap:
        idx = 0
        cnt = 1
        mid_gap = (high_gap + low_gap) // 2
        while True:
            val = lst[idx]
            next_val = val + mid_gap
            next_idx = bisect_left(lst, next_val)
            if next_idx < N:
                cnt += 1
                idx = next_idx
            else:
                break
        
        if cnt < C:
            high_gap = mid_gap - 1
        else:
            low_gap = mid_gap + 1
            answer = mid_gap
    return answer

N, C = list(map(int, input().split()))
lst = []
for _ in range(N):
    lst.append(int(input()))
print(main(lst, N, C))