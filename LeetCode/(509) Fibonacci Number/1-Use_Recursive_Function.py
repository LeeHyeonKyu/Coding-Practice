class Solution:
    def fib(self, n: int) -> int:
        if n <= 1 :
            return n
        else :
            return self.fib(n-1) + self.fib(n-2)

'''
Runtime : 796 ms
Memory : 14.2 MB
'''
