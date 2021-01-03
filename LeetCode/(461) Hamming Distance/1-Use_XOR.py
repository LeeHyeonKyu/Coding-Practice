class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

'''
Runtime : 52 ms
Memory : 14.2 MB
'''
