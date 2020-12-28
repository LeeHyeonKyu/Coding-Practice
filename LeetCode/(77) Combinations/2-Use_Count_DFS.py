class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results =[]
        
        def dfs(elements, start: int, k: int) :
            if k == 0 :
                results.append(elements[:])
                
            # 이전 값은 고정하여 재귀호출
            for i in range(start, n+1) :
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
            pass # end dfs
        
        dfs([], 1, k)
        return results

'''
Runtime : 468 ms
Memory : 15.8 MB
'''
