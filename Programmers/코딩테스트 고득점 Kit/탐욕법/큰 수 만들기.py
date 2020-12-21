def solution(number, k) :
    stack = []
    for n in number :
        while True :
            if len(stack) == 0 :
                stack.append(n)
                break
            elif stack[-1] < n and k > 0 :
                stack.pop()
                k -= 1
            else :
                stack.append(n)
                break
    
    if k > 0 :
        stack = stack[:-k]
    
    return ''.join(stack)
