class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for idx, temper in enumerate(T) :
            while stack and stack[-1][0] < temper :
                low_temper = stack.pop()
                answer[low_temper[1]] = idx - low_temper[1]
            stack.append((temper, idx,))
        return answer

'''
Runtime : 528 ms
Memory : 19.4 MB
'''
