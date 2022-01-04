def solution(s):
    prev = ' '
    answer = ''
    for char in s:
        if prev == ' ':
            char = char.upper()
        else:
            char = char.lower()
        prev = char
        answer += char
    return answer