class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        idx = 0
        for x, y in points :
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))
            idx += 1
            
        result = []
        for _ in range(K) :
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])
            
        return result

'''
Runtime : 652 ms
Memory : 20.6 MB
'''
