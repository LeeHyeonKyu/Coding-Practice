class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n <= 1 :
            return n
        
        if self.dp[n] :
            return self.dp[n]
        else :
            self.dp[n] = self.fib(n-1) + self.fib(n-2)
            return self.dp[n]

'''
Runtime : 24 ms
Memory : 14.2 MB
'''
