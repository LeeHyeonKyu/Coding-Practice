class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        # pivot 값의 인덱스 생성
        for i in range(len(nums)-2) :
            # pivot 값이 이전과 동일할 경우 continue
            if i > 0 and nums[i] == nums[i-1] :
                continue
            left = i+1
            right = len(nums)-1
            while left < right :
                # 합산 값에 따라 포인터 조정
                cal_sum = nums[i] + nums[left] + nums[right]
                if cal_sum < 0 :
                    left += 1
                elif cal_sum > 0 :
                    right -= 1
                else :
                    answer.append([nums[i], nums[left], nums[right]])
                    # 비교 값이 달라질 때까지 포인터 이동
                    while left < right and nums[left] == nums[left+1] :
                        left += 1
                    while left < right and nums[right] == nums[right-1] :
                        right -= 1
                    left += 1
                    right -= 1
        
        return answer

'''
Runtime : 844 ms
Memory : 17.5 MB
'''
