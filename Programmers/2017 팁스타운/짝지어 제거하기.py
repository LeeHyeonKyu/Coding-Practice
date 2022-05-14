from collections import defaultdict

def solution(s):
    char_dict = defaultdict(list)
    flags = [False] * len(s)
    for idx, char in enumerate(s):
        if len(char_dict[char]) > 0:
            front = char_dict[char].pop()
            if all(flags[front+1:idx]):
                flags[front] = True
                flags[idx] = True
            else:
                char_dict[char].append(front)
                char_dict[char].append(idx)
        else:
            char_dict[char].append(idx)
    
    return 1 if all(flags) else 0