import collections

def solution(cacheSize, cities):
    cache = collections.deque([], cacheSize)
    answer = 0
    cities = [x.lower() for x in cities]
    for city in cities :
        if city not in cache :
            cache.append(city)
            answer += 5
        else :
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer
