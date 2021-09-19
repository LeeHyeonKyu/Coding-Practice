def change_word(char):
    if char == 'A':
        char = 'E'
    elif char == 'E':
        char = 'I'
    elif char == 'I':
        char = 'O'
    elif char == 'O':
        char = 'U'
    elif char == 'U':
        char = 'X'
    return char

def solution(word):
    new, cnt = ['A'], 1
    word = list(word)

    while new != word:
        if len(new) != 5:
            new += 'A'
        else:
            new[-1] = change_word(new[-1])
        while new[-1] == 'X':
            new.pop()
            new[-1] = change_word(new[-1])
        cnt += 1
    
    return cnt