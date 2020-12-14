def solution(n):
    return int(''.join(sorted([s for s in str(n)], reverse=True)))
