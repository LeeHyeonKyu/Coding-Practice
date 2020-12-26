class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for idx, char in enumerate(s) :
            # 이미 등장했던 문자라면 start의 위치 갱신
            if char in used and start <= used[char] :
                start = used[char] + 1
            # 아닌 경우 최대 부분 문자열 길이 갱신
            else :
                max_length = max(max_length, idx - start + 1)
            
            # 현재의 문자 위치 삽입
            used[char] = idx
            
        return max_length

'''
Runtime : 56 ms
Memory : 14.5 MB
'''
