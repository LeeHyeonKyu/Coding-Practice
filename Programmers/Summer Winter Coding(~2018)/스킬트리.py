import math

def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees :
        tmp = []
        for s in skill :
            tmp.append(math.inf if skill_tree.find(s) == -1 else skill_tree.find(s)) 
        if tmp == sorted(tmp) :
            cnt += 1
        
    return cnt
