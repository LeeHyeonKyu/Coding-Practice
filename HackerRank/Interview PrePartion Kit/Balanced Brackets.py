def isBalanced(s):
    stack = []
    bracket_map = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    if len(s) == 0 :
        return 'YES'
    
    for bracket in s :
        if not bracket in bracket_map :
            stack.append(bracket)
        else :
            if len(stack) == 0 :
                return 'NO'
            else :
                check = stack.pop()
                if not bracket_map[bracket] == check :
                    return 'NO'
    
    if stack :
        return 'NO'
    
    return 'YES'
