class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        answer = 0
        for price in prices :
            while len(stack) > 0 and stack[-1] > price :
                stack.pop()
            stack.append(price)
            answer = max(answer, price - stack[0])
        return answer

'''
Runtime : 68 ms
Memory : 15.1 MB
'''
