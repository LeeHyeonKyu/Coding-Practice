class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([j for j in stones if j in jewels])

'''
Runtime : 32 ms
Memory : 14.4 MB
'''
