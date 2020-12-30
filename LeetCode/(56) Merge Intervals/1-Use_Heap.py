class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        result = []
        
        while intervals :
            tmp = heapq.heappop(intervals)
            if len(result) == 0 or result[-1][1] < tmp[0]:
                result.append(tmp)
            elif result[-1][1] >= tmp[0] :
                result[-1][1] = max(result[-1][1], tmp[1])
        
        return result

'''
Runtime : 92 ms
Memory : 16.1 MB
'''
