class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        for i in s :
            if i not in map :
                stack.append(i)
            elif not stack or map[i] != stack.pop() :
                return False
        
        return len(stack) == 0

'''
Runtime : 20 ms
Memory : 14.2 MB
'''
