class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_idx, i in enumerate(nums[:-1]) :
            for j_idx, j in enumerate(nums[i_idx+1:]) :
                if i + j == target :
                    return [i_idx, i_idx + j_idx + 1]
