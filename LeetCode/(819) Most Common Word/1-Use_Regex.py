class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        data = re.sub('[^\w]', ' ', paragraph.lower()).split()
        c_data = collections.Counter(data)
        for char, _ in c_data.most_common() :
            if char not in banned :
                return char

'''
Runtime : 36 ms
Memory : 14.2 MB
'''
