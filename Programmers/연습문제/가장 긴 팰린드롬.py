def solution(s):
    def two_pointer(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    answer = 0
    for idx in range(len(s)):
        answer = max(answer, two_pointer(idx, idx+1), two_pointer(idx, idx+2))
    return answer