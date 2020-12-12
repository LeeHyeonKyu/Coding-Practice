def solution(s):
    answer = []
    split_s = s.split(' ')
    for char in split_s :
        trans_char = []
        for idx, string in enumerate(char) :
            if idx % 2 == 0 :
                trans_char.append(string.upper())
            else :
                trans_char.append(string.lower())
        answer.append(''.join(trans_char))
            
    return ' '.join(answer)
