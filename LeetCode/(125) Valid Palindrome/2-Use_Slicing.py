class Solution:
    def isPalindrome(self, s: str) -> bool:
        work_lst = []
        for string in s :
            if string.isalpha() :
                work_lst.append(string.lower())
            elif string.isdigit() :
                work_lst.append(string)
        return work_lst == work_lst[::-1]
        
'''
Runtime : 48 ms
Memory : 20.1 MB
'''
