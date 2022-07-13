def solution(s):
    flag = True
    while flag:
        stack = []
        for char in s:
            if len(stack) > 0 and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        if len(stack) == len(s):
            flag = False
        elif len(stack) == 0:
            return 1
        else:
            s = ''.join(stack)
    return 0