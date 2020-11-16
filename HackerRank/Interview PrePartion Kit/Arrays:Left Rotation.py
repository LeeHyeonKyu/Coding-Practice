def rotLeft(a, d):
    answer = a[d:]
    answer.extend(a[:d])
    return answer
