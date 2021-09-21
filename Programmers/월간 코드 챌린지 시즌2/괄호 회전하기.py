def check(lst):
    stack = []
    brackets = {")":"(", "}":"{", "]":"["}
    for b in lst:
        if b in brackets:
            if len(stack) == 0:
                return 0
            else:
                last_b = stack.pop()
                if brackets[b] != last_b:
                    return 0
        else:
            stack.append(b)
    if len(stack) > 0:
        return 0
    else:
        return 1

def rotate(lst, num):
    return lst[num:] + lst[:num]

def solution(s):
    answer = 0
    for i in range(len(s)):
        lst = rotate(s, i)
        answer += check(lst)
    return answer