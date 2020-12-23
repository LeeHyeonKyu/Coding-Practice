class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs :
            anagrams[''.join(sorted(word))].append(word)
        
        return anagrams.values()

'''
Runtime : 100 ms
Memory : 17.8 MB
'''
