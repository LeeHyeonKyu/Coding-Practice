class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        result = []
        
        # 키 역순, 인덱스 삽입
        for height, index in people :
            heapq.heappush(heap, [-height, index])
            
        while heap :
            height, index = heappop(heap)
            result.insert(index, [-height, index])
        
        return result

'''
Runtime : 100 ms
Memory : 14.4 MB
'''
