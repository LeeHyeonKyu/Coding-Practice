def solution(s):
    stack = []
    for i in s :
        if i == "(" :
            stack.append(i)
        else :
            try :
                stack.pop()
            except :
                return False
    
    return len(stack) == 0
