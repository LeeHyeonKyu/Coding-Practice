class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

'''
Runtime : 264 ms
Memory : 16.7 MB
'''
