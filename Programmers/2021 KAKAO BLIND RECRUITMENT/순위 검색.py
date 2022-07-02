class Person():
    def __init__(self, lang, position, career, food, score):
        self.lang = lang
        self.position = position
        self.career = career
        self.food = food
        self.score = int(score)

def solution(infos, queries):
    lst = []
    for info in infos:
        lang, position, career, food, score = info.split()
        lst.append(Person(lang, position, career, food, score))
    
    answer = []
    for query in queries:
        cnt = 0
        l, p, c, fs = query.split(' and ')
        f, s = fs.split()
        for person in lst:
            if l == '-' or person.lang == l:
                if p == '-' or person.position == p:
                    if c == '-' or person.career == c:
                        if f == '-' or person.food == f:
                            if int(s) <= person.score:
                                cnt += 1
        answer.append(cnt)