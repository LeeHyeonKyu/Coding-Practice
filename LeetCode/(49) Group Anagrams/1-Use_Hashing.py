class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dic = {}
        for char in strs :
            sorted_char = ''.join(sorted(char))
            if sorted_char not in char_dic.keys() :
                char_dic[sorted_char] = [char,]
            else :
                char_dic[sorted_char].append(char)
        
        answer = []
        for key, value in char_dic.items() :
            answer.append(value)
        
        return answer

'''
Runtime : 92 ms
Memory : 17 MB
'''
