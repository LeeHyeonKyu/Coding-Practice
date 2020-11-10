import heapq

def solution(jobs):
    answer = 0
    require_heap = []
    work_heap = []
    time = 0
    now_working = 0
    req_time = 0
    finish_time = []
    work_count = 0

    for require, work in jobs :
        heapq.heappush(require_heap, (require, work))
        pass

    ready_req = heapq.heappop(require_heap)
    while True :
        while time == ready_req[0] :
            heapq.heappush(work_heap, (ready_req[1], ready_req[0]))
            if len(require_heap) != 0 :
                ready_req = heapq.heappop(require_heap)
            elif len(require_heap) == 0 :
                break
                pass
            pass

        if work_count != 0 and now_working == 1 :
            finish_time.append(time - req_time)
            now_working -= 1
            pass

        if now_working == 0 and len(work_heap) != 0 :
            now_working, req_time = heapq.heappop(work_heap)
            work_count += 1
        elif now_working != 0 :
            now_working -= 1
        elif now_working + len(require_heap) + len(work_heap) == 0 :
            break

        time += 1
        pass

    answer = int(sum(finish_time) / work_count)

    return answer
