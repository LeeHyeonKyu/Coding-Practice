def solution(k, dungeons):
    max_cnt = 0
    length = len(dungeons)
    flags = [True] * length
    results = [(k, max_cnt, flags)]
    
    def search(now, cnt, flags):
        tmp_flags = flags[:]
        if tmp_flags[i] and dungeons[i][0] <= now:
            tmp_flags[i] = False
            now -= dungeons[i][1]
            cnt += 1
            results.append((now, cnt, tmp_flags))
        return cnt
    
    while results:
        now, cnt, flags = results.pop()
        for i in range(length):
            tmp_cnt = search(now, cnt, flags)
            max_cnt = max(max_cnt, tmp_cnt)
    return max_cnt