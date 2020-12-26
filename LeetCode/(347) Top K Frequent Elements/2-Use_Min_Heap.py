class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        topk = []
        
        # heap에 음수로 삽입
        for f in freqs :
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        for _ in range(k) :
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk

'''
Runtime : 100 ms
Memory : 18.7 MB
'''
