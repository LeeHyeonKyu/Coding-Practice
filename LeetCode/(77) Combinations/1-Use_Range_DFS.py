class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = []
        
        def dfs(lst) :
            if len(comb) == k :
                result.append(comb[:])
            
            for i in lst :
                comb.append(i)
                dfs(list(range(i+1, n+1)))
                comb.pop()
                
            pass # end dfs
        
        dfs(list(range(1, n+1)))
        return result

'''
Runtime : 568 ms
Memory : 16 MB
'''
