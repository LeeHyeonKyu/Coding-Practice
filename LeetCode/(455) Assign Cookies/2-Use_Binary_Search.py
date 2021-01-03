class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        result = 0 
        for i in s : 
            # 이진 검색으로 더 큰 인덱스 탐색
            index = bisect.bisect_right(g, i)
            if index > result : 
                result += 1
        
        return result

'''
Runtime : 164 ms
Memory : 16 MB
'''
