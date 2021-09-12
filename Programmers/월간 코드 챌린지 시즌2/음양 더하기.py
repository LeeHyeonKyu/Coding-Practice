def solution(absolutes, signs):
    result = 0
    for num, flag in zip(absolutes, signs):
        if flag:
            result += num
        else:
            result -= num
    return result