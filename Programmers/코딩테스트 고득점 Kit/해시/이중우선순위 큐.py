import heapq

def solution(operations) :
    heap = []
    for o in operations :
        if 'I' in o :
            heapq.heappush(heap, int(o[2:]))
        elif 'D 1' == o and len(heap) > 0 :
            heap.pop()
        elif 'D -1' == o and len(heap) > 0 :
            heapq.heappop(heap)

    if len(heap) == 0 :
        answer = [0,0]
    elif len(heap) == 1 :
        min_num = heapq.heappop(heap)
        answer = [min_num,min_num]
    else :
        heap.sort()
        max_num = heap.pop()
        min_num = heapq.heappop(heap)
        answer = [max_num,min_num]

    return answer
