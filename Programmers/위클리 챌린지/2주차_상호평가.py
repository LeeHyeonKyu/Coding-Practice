def solution(scores):
    answer = []
    for idx, score in enumerate(scores):
        wo_score = score[:idx] + score[idx+1:]
        num_student = len(wo_score)
        sum_score = sum(wo_score)
        if score[idx] < max(wo_score) and score[idx] > min(wo_score):
            num_student += 1
            sum_score += score[idx]
        student_score = sum_score / num_student

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