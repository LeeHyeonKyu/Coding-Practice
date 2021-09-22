def algorithm_u(brackets):
    result = []
    for idx, bracket in enumerate(brackets):
        if idx == 0 or idx == len(brackets)-1:
            pass
        elif bracket == '(':
            result.append(')')
        elif bracket == ')':
            result.append('(')
    return ''.join(result)

def chk_right(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        else:
            return False
    return True

def devide(brackets):
    ocnt, ccnt = 0, 0
    for idx, bracket in enumerate(brackets):
        if bracket == '(':
            ocnt += 1
        elif bracket == ')':
            ccnt += 1
        
        if ocnt == ccnt:
            u = brackets[:idx+1]
            v = brackets[idx+1:]
            return u, v

def solution(p):
    if p == '':
        return p
    
    u, v = devide(p)
    if chk_right(u):
        v = solution(v)
        return u + v
    else:
        v = solution(v)
        u = algorithm_u(u)
        return '(' + v + ')' + u