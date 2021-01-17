import collections

def solution(answers):
    # 학생별로 패턴 초기화
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer_cnt = collections.defaultdict(int)
    
    # 순회하며 각 패턴과 일치하는지 확인 및 누적
    for idx, num in enumerate(answers) :
        if num == p1[idx % 5] :
            answer_cnt[1] += 1
        if num == p2[idx % 8] :
            answer_cnt[2] += 1
        if num == p3[idx % 10] :
            answer_cnt[3] += 1
    
    # 누계의 최대값과 같은 사람을 결과로 반환
    result = []
    max_val = max(answer_cnt.values())
    for key, val in answer_cnt.items() :
        if val == max_val :
            result.append(key)

    return sorted(result)
