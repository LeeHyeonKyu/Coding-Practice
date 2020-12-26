class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        most_common = counter.most_common()
        answer = []
        for i in range(k) :
            answer.append(most_common[i][0])
        return answer

'''
Runtime : 96 ms
Memory : 18.8 MB
'''
