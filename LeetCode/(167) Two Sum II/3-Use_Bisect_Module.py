class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers) :
            expacted = target - num
            start_to_search = idx + 1
            find_point = bisect.bisect_left(numbers, expacted, lo=start_to_search)
            if find_point < len(numbers) and numbers[find_point] == expacted :
                return [idx+1, find_point+1]

'''
Runtime : 88 ms
Memory : 14.8 MB
'''
