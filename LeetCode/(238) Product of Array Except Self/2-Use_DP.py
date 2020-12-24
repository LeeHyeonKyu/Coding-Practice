class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        
        # 왼쪽부터 곱셈
        p = 1
        for i in range(0, len(nums)) :
            out.append(p)
            p = p * nums[i]
        
        # 오른쪽부터 곱셈
        p = 1
        for i in range(len(nums)-1, -1, -1) :
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out

'''
Runtime : 228 ms
Memory : 20.9 MB
'''
