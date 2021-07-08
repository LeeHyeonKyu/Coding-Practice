import heapq

def whatFlavors(cost, money):
    answer = []
    heap = []
    for idx, val in enumerate(cost) :
        heap.append((val, idx))
    heapq._heapify_max(heap)
    while heap :
        pivot = heapq._heappop_max(heap)
        for compare in heap :
            if pivot[0] + compare[0] == money :
                answer = [min(pivot[1],compare[1]), max(pivot[1],compare[1])]
                break
        if answer :
            break
                
    print(answer[0]+1, answer[1]+1)
