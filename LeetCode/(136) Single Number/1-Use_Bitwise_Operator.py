class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums :
            result ^= num
        return result

'''
Runtime : 152 ms
Memory : 16.8 MB
'''
