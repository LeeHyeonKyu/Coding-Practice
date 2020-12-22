from itertools import filterfalse

def iterative_bfs(start, graph, target, cnt=0) :
    discovered = [start,]
    queue = [start,]
    cnt = 0
    while queue :
        v = queue.pop(0)
        cnt += 1
        for w in graph[v] :
            if w not in discovered :
                discovered.append(w)
                queue.append(w)
            if w == target :
                return cnt
    return 0

def solution(begin, target, words):
    answer = 0
    word_graph = {}
    word_len = len(words[0])
    near_lst = []
    
    for word in words :
        zip_word = list(zip(begin, word))
        wrong_zip = filterfalse(lambda x : x[0] == x[1], zip_word)
        wrong_count = len(list(wrong_zip))
        if wrong_count == 1 :
            near_lst.append(word)
            pass
        pass 
    word_graph[begin] = near_lst
    
    for pivot_word in words :
        near_lst = []
        for compare_word in words :
            zip_word = list(zip(pivot_word, compare_word))
            wrong_zip = filterfalse(lambda x : x[0] == x[1], zip_word)
            wrong_count = len(list(wrong_zip))
            if wrong_count == 1 :
                near_lst.append(compare_word)
                pass
            pass 
        word_graph[pivot_word] = near_lst
        pass
    
    answer = iterative_bfs(begin, word_graph, target)
    
    return answer
