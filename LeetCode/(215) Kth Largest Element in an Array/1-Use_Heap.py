class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

'''
Runtime : 56 ms
Memory : 15.2 MB
'''
