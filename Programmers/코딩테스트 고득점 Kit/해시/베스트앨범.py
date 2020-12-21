def solution(genres, plays) :
    sum_dict = {}
    com_dict = {}
    answer = []
    for idx, g in enumerate(genres) :
        if g in com_dict.keys() :
            com_dict[g].append((idx, plays[idx]))
            sum_dict[g] += plays[idx]
        else :
            com_dict[g] = [(idx, plays[idx])]
            sum_dict[g] = plays[idx]
    
    sum_lst = sorted(sum_dict.items(), key=lambda x : x[1], reverse=True)
    for g, _ in sum_lst :
        com_lst = sorted(com_dict[g], key=lambda x : x[1], reverse=True)
        answer.append(com_lst[0][0])
        if len(com_lst) > 1 :
            answer.append(com_lst[1][0])

    return answer
