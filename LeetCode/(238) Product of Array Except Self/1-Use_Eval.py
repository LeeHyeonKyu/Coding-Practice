class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        nums = [str(x) for x in nums]
        for i in range(len(nums)) :
            result.append(eval('*'.join(nums[:i] + nums[i+1:])))
        return result

'''
Time Limit Exceeded
'''
