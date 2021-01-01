class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

'''
Runtime : 48 ms
Memory : 15 MB
'''
