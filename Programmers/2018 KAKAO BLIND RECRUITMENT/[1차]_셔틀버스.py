import heapq

def solution(n, t, m, timetable):
    timetable = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    heapq.heapify(timetable)
    time, cnt = 9 * 60, 0
    for _ in range(n) :
        try :
            while cnt < m and timetable[0] <= time :
                last_man = heapq.heappop(timetable)
                cnt += 1
            last_cnt = cnt
            cnt = 0
            time += t
        except :
            HH, MM = divmod(540 + (t * (n-1)), 60)
            return str(HH).zfill(2) + ':' + str(MM).zfill(2)
    
    if last_cnt < m :
        HH, MM = divmod(540 + (t * (n-1)), 60)
        return str(HH).zfill(2) + ':' + str(MM).zfill(2)
    else :
        HH, MM = divmod(last_man - 1, 60)
        return str(HH).zfill(2) + ':' + str(MM).zfill(2)
