class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

'''
Runtime : 96 ms
Memory : 18.7 MB
'''
