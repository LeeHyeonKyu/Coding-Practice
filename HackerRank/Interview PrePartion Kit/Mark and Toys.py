def maximumToys(prices, k):
    cnt = 0
    prices_lst = sorted(prices)
    for price in prices_lst :
        if k - price >= 0 :
            cnt += 1
            k -= price
        else :
            break
    return cnt
