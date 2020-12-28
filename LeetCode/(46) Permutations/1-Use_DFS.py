class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []
        
        def dfs(elements) :
            # 리프 노드인 경우 결과 추가
            if len(elements) == 0 :
                results.append(prev_elements[:])
            
            # 순열 생성 재귀 호출
            for e in elements :
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
            pass # end dfs
        
        dfs(nums)
        return results

'''
Runtime : 36 ms
Memory : 14.4 MB
'''