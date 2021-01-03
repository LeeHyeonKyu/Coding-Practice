class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)

'''
Runtime : 228 ms
Memory : 20.6 MB
'''
