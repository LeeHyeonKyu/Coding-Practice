class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(lst) :
            if sum(comb) == target :
                results.append(comb[:])
            elif sum(comb) > target :
                return
            
            for idx, num in enumerate(lst) :
                comb.append(num)
                dfs(lst[idx:])
                comb.pop()
            pass # end dfs
        
        results = []
        comb = []
        dfs(candidates)
        return results

'''
Runtime : 124 ms
Memory : 14.4 MB
'''
