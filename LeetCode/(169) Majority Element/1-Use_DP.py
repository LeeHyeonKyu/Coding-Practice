class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        for num in nums :
            if counter[num] == 0 :
                counter[num] = nums.count(num) * 2
            if counter[num] >= len(nums) :
                return num

'''
Runtime : 164 ms
Memory : 15.5 MB
'''
