from collections import defaultdict

def solution(table, languages, preference):
    dic = defaultdict(int)
    for lst in table:
        lst = lst.split()
        job = lst.pop(0)
        for idx, language in enumerate(lst):
            if language in languages:
                dic[job] += ((5-idx) * preference[languages.index(language)])
    
    return sorted(dic.keys(), key=lambda x: (-dic[x], x))[0]