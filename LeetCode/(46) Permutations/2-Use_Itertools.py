class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))

'''
Runtime : 36 ms
Memory : 14.3 MB
'''
