class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        com_lst = itertools.combinations(nums, 3)
        answer = []
        for com in com_lst :
            if sum(com) == 0 and sorted(list(com)) not in answer :
                answer.append(sorted(list(com)))
        return answer

'''
Time Limit Exceeded
'''
