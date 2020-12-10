def solution(s, n):
    answer = []
    for char in s :
        if char.isupper() :
            secret_char = (ord(char) + n)
            if secret_char > 90 :
                secret_char -= 26
            answer.append(chr(secret_char))
        elif char.islower() :
            secret_char = (ord(char) + n)
            if secret_char > 122 :
                secret_char -= 26
            answer.append(chr(secret_char))
        else :
            answer.append(char)
    
    return ''.join(answer)
