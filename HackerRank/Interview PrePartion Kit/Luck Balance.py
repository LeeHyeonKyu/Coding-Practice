def luckBalance(k, contests):
    total_luck = 0
    for luck,important in sorted(contests, reverse=True):
        if not important:
            total_luck += luck
        elif k:
            total_luck += luck
            k -= 1
        else:
            total_luck -= luck
    return total_luck

    return answer
