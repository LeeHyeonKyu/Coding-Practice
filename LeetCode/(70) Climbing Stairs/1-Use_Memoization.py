class Solution:
    dp = collections.defaultdict(int)
    
    def climbStairs(self, n: int) -> int:
        if n <= 2 :
            return n
        
        if self.dp[n] :
            return self.dp[n]
        else :
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dp[n]

'''
Runtime : 32 ms
Memory : 14.4 MB
'''
