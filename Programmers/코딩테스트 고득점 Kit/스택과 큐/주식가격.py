def solution(prices : list) -> list :
    answer = []
    temp_lst = [0] * len(prices)
    stack = []
    time = -1

    for idx, price in enumerate(prices) :
        time += 1
        if idx == 0 :
            stack.append((price, idx))
        elif price >= stack[-1][0] :
            stack.append((price, idx))
        elif price < stack[-1][0] :
            while stack :
                before_price, before_idx = stack.pop()
                if price < before_price :
                    temp_lst[before_idx] = time - before_idx
                    before_idx += 1
                elif price >= before_price :
                    stack.append((before_price, before_idx))
                    stack.append((price, idx))
                    break
                    pass

                if len(stack) == 0 :
                    stack.append((price, idx))
                    break
                    pass
                pass
            pass

    for price, idx in stack :
        temp_lst[idx] = time - idx
        pass

    answer = temp_lst

    return answer
