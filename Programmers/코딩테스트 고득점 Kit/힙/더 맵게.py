import heapq

def solution(scoville:list, K:int) -> int:
    heap = scoville
    heapq.heapify(heap)
    cnt = 0
    min1_sc = heapq.heappop(heap)

    if min1_sc >= K :
        return 0

    while heap :
        cnt += 1
        min2_sc = heapq.heappop(heap)
        new_sc = min1_sc + (min2_sc * 2)
        heapq.heappush(heap, new_sc)
        min1_sc = heapq.heappop(heap)
        if min1_sc >= K :
            return cnt
            pass

    return -1
