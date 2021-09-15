def solution(nums):
    can_get = len(nums) // 2
    nums = set(nums)
    if len(nums) >= can_get:
        return can_get
    else:
        return len(nums)