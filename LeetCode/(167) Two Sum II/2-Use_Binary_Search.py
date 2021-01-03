class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers) :
            expacted = target - num
            left = idx + 1
            right = len(numbers) - 1
            while left <= right :
                mid = (left + right) // 2
                if numbers[mid] < expacted :
                    left = mid + 1
                elif numbers[mid] > expacted :
                    right = mid - 1
                else :
                    return [idx+1, mid+1]

'''
Runtime : 108 ms
Memory : 14.8 MB
'''
