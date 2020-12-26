class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        answer = 0
        for j in jewels :
            answer += counter[j]
        return answer

'''
Runtime : 40 ms
Memory : 14.1 MB
'''
