class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for idx, temper in enumerate(T) :
            while stack and T[stack[-1]] < temper :
                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)
        return answer

'''
Runtime : 500 ms
Memory : 18.8 MB
'''
