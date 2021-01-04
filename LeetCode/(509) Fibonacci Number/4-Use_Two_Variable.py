class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(0, n) :
            a, b = b, a + b
        return a

'''
Runtime : 24 ms
Memory : 14.1 MB
'''
