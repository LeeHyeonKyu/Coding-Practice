import collections

def solution(str1, str2):
    new_1, new_2 = [], []
    
    for i in range(1, len(str1)) :
        if str1[i-1].isalpha() and str1[i].isalpha() :
            new_1.append(str1[i-1].lower() + str1[i].lower())

    for i in range(1, len(str2)) :
        if str2[i-1].isalpha() and str2[i].isalpha() :
            new_2.append(str2[i-1].lower() + str2[i].lower())
    
    counter_1 = collections.Counter(new_1)
    counter_2 = collections.Counter(new_2)
    
    inter_counter = collections.Counter(counter_1 & counter_2)
    union_counter = collections.Counter(counter_1 | counter_2)
    
    inter_val = sum(inter_counter.values())
    union_val = sum(union_counter.values())
    
    try :
        return int((inter_val / union_val) * 65536)
    except :
        return 1 * 65536
