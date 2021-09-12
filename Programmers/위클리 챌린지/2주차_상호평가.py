from collections import defaultdict

def solution(scores):
    dic = defaultdict(list)
    answer = []
    
    for i, lst in enumerate(scores):
        for j, score in enumerate(lst):
            if i == j:
                pass
            else:
                dic[j].append(score)

    for student in sorted(dic.keys()):
        score = dic[student]
        self_score = scores[student][student]
        if self_score <= max(score) and self_score >= min(score):
            student_score = (sum(score) + self_score) / (len(score) + 1)
        else:
            student_score = sum(score) / len(score)

        if student_score >= 90:
            answer.append('A')
        elif student_score >= 80:
            answer.append('B')
        elif student_score >= 70:
            answer.append('C')
        elif student_score >= 50:
            answer.append('D')
        else:
            answer.append('F')

    return ''.join(answer)