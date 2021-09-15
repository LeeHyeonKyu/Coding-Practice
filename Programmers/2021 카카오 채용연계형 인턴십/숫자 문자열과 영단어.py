def solution(s):
    answer = []
    alphabet = []
    lst = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for char in s:
        if char.isdigit():
            answer.append(char)
        else:
            alphabet.append(char)
        
        if ''.join(alphabet) in lst:
            answer.append(str(lst.index(''.join(alphabet))))
            alphabet = []
    
    return int(''.join(answer))