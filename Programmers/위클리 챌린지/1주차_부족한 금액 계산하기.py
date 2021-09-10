def solution(price, money, count):
    require_money = price * count * (count+1) // 2
    if money >= require_money:
        return 0
    else:
        return require_money - money