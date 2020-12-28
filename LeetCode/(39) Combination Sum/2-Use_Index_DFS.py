class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(csum, index, path) :
            # 종료 조건
            if csum < 0 :
                return
            if csum == 0 :
                result.append(path)
                return
            
            # 자신부터 하위 원소까지의 나열 재귀 호출
            for i in range(index, len(candidates)) :
                dfs(csum - candidates[i], i, path + [candidates[i]])
            pass # end dfs
        
        result = []
        dfs(target, 0, [])
        return result

'''
Runtime : 80 ms
Memory : 14.2 MB
'''
