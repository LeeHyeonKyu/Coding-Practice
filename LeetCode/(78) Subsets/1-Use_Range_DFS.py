class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, sub_set_len) :
            # 종료 조건
            if len(sub_set) == sub_set_len :
                result.append(sub_set[:])
                return

            # 현재 포인트 다음부터 재귀 호출
            for point in range(start, len(nums)) :
                sub_set.append(nums[point])
                dfs(point+1, sub_set_len)
                sub_set.pop()

            pass # end dfs
        
        result = []
        sub_set = []
        for count in range(len(nums)+1) :
            dfs(0, count)
        return result

'''
Runtime : 28 ms
Memory : 14.3 MB
'''
