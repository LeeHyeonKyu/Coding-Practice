class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        tmp = []
        for char in s :
            if not tmp or char not in tmp:
                tmp.append(char)
            else : 
                answer = max(answer, len(tmp))
                tmp = tmp[tmp.index(char)+1:]
                tmp.append(char)
        answer = max(answer, len(tmp))
        return answer

'''
Runtime : 108 ms
Memory : 14.4 MB
'''
