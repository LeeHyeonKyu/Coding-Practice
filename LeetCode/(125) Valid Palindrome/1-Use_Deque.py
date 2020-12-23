class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        
        for char in s :
            if char.isalnum() :
                strs.append(char.lower())
        
        while len(strs) > 1 :
            if strs.popleft() != strs.pop() :
                return False
        
        return True

'''
Runtime : 52 ms
Memory : 19.2 MB
'''
