class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for i in range(len(nums)-k+1) :
            answer.append(max(nums[i:i+k]))
        return answer

'''
Time Limit Exceeded
'''
