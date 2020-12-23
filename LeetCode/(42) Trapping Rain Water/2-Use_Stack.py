class Solution:
    def trap(self, height) -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)) :
            # 변곡점을 만났을 때 실행되는 loop문
            while stack and height[i] > height[stack[-1]] :
                top = stack.pop()
                if not len(stack) :
                    break
                    
                # 이전과의 거리와 높이 차이를 계산하여 합산
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters
            
            stack.append(i)
        
        return volume

'''
Runtime : 60 ms
Memory : 14.8 MB
'''
