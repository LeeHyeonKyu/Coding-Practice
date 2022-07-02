from math import ceil

def solution(n, words):
    answer = [0,0]
    used = set()
    prev_char = words[0][0]
    for cnt, word in enumerate(words, 1):
        if word in used or word[0] != prev_char:
            r = n if cnt % n == 0 else cnt % n
            q = ceil(cnt / n)
            answer = [r, q]
            break
        used.add(word)
        prev_char = word[-1]
    
    return answer